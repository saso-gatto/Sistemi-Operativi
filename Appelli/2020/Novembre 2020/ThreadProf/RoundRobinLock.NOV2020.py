from threading import Thread,RLock,Condition
from random import randint

debug = True

class RoundRobinLock:
    
    def __init__(self,N : int):
        self.nturni = N
        self.presidentGroupID = -1
        self.lock = RLock()
        self.conditions = [Condition(self.lock) for _ in range(0,N)]
        self.inAttesa = [0 for _ in range(0,N)]
        self.turnoCorrente = 0
        self.possessori = 0  #uso un count per verificare se è possibile acquisire un microfono
        self.presidentsWaiting=0
#
# Non c'è bisogno di particolare attenzione alla gestione del primo accesso
#
    
    def acquire(self,id : int):
        with self.lock:
            self.inAttesa[id] += 1
            while( self.possessori > 0 and self.turnoCorrente != id or self. presidentsWaiting>0 and id!=self.presidentGroupID):
                self.conditions[id].wait()
                
            self.inAttesa[id] -= 1
            self.possessori += 1
            if debug:
                self.__print__()
            
    
    def release(self,id : int):
        with self.lock:
            #
            #lasciare il lock e cercare eventualmente il prossimo turno
            #
            self.possessori -= 1
            if self.possessori == 0:
                #aggiornare turno corrente e fare notify
                #for su quelli inAttesa
                if self.turnoCorrente==self.presidentGroupID:
                    self.turnoCorrente=self.turnoSospeso
                if self.presidentsWaiting ==0:
                    for i in range(1,self.nturni):          #Parto da 1 perché cosi salto l'id corrente dal controllo
                        turno = (id + i) % self.nturni      #Testo tutti i turni presenti alla mia desta
                        if self.inAttesa[turno] > 0:        #Se il turno alla mia destra è in attesa, risveglio quel turno
                            self.turnoCorrente = turno
                            self.conditions[turno].notify_all()
                            break
                else:
                    self.turnoSospeso=self.turnoCorrente
                    self.turnoCorrente= self.presidentGroupID
                    self.conditions[self.presidentGroupID].notify_all()
            if debug:
                self.__print__()

    def setPresident(self,idP: int):
        with self.lock:
            self.president= idP

    def urgentAcquire (self):
        with self.lock:
            self.presidentsWaiting+=1
            while self.turnoCorrente!=self.presidentGroupID and self.possessori>0:
                self.conditions[self.presidentGroupID].wait()
            self.presidentsWaiting-=1
            self.possessori+=1

    def __print__(self):
        with self.lock:
            print("=" * self.turnoCorrente + "|@@|" + "=" * (self.nturni - self.turnoCorrente -1) )
            for l in range(0,max(max(self.inAttesa),self.possessori)):
                o = ''
                for t in range(0,self.nturni):
                    if self.turnoCorrente == t: 
                        if self.possessori > l:
                            o = o + "|o"
                        else:
                            o = o + "|-"
                    if self.inAttesa[t] > l:
                        o = o + "*"
                    else:
                        o = o + "-"
                    if self.turnoCorrente == t:
                        o = o + "|"
                print (o) 
            print("")       

class RoundRobinLockStarvationMitigation(RoundRobinLock):
    
    SOGLIASTARVATION = 5
    
    def __init__(self,N : int):
        super().__init__(N)
        self.consecutiveOwners = 0

    
    def acquire(self,id : int):
        with self.lock:
            self.inAttesa[id] += 1
            while( self.possessori > 0 and 
                   self.turnoCorrente != id or 
                   self.turnoCorrente == id and 
                   self.consecutiveOwners > self.SOGLIASTARVATION and
                   max(self.inAttesa) > 0  
                 ):
                self.conditions[id].wait()
                
            self.inAttesa[id] -= 1
            self.possessori += 1
            self.consecutiveOwners += 1
            if debug:
                self.__print__()
            
    
    def release(self,id : int):
        with self.lock:
            self.possessori -= 1
            if self.possessori == 0:
                for i in range(1,self.nturni):
                    turno = (id + i) % self.nturni
                    if self.inAttesa[turno] > 0:
                        self.turnoCorrente = turno
                        self.consecutiveOwners = 0
                        self.conditions[turno].notifyAll()
                        break 

    
class RoundRobinLockConCoda(RoundRobinLock):
    
    def __init__(self,N : int):
        pass
    
    def acquire(self,id : int):
        pass
    
    def release(self,id : int):
        pass
    
    
class Animale(Thread):

    def __init__(self,id: int, idTurno : int, R : RoundRobinLock):
        super().__init__()
        self.idTurno = idTurno
        self.iterazioni = 1000
        self.lock = R

    def run(self):
        while(self.iterazioni > 0):
                self.iterazioni -= 1
                self.lock.acquire(self.idTurno)
                #self.lock.__print__()
                self.lock.release(self.idTurno)


NGruppi = 5        
R = RoundRobinLockStarvationMitigation(NGruppi)
#R = RoundRobinLock(NGruppi)
for i in range(0,60):
    Animale(i,randint(0,NGruppi-1),R).start()

 
                
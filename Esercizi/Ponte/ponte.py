from threading import Thread,Lock,Condition
from time import sleep
from random import randrange

class Ponte:
    def __init__(self):
        self.direzione=False          # True=Mare  False=Montagna 
        self.lock = Lock ()     #Il lock deve gestire l'attesa dei turisti
        self.conditionMare= Condition(self.lock)
        self.conditionMonte = Condition(self.lock)
        self.turistiSulPonte= 0

    def getTuristiPonte (self):
        return self.turistiSulPonte

    def getDirection(self):
        return self.direzione
    
    def setDirection(self,d):
        self.direzione = d
     
    def acquirePonteMare(self): #dir==True --> Mare
        with self.lock:
            while (self.direzione == False): #Se il ponte è occupato da una dir. diversa
                self.conditionMare.wait()
            self.turistiSulPonte+=1

    def acquirePonteMonte(self):
        with self.lock:
            while (self.direzione ==True): #Se il ponte è occupato da una dir. diversa
                self.conditionMonte.wait()  
            self.turistiSulPonte+=1          
    
    def releasePonteMare(self):
        with self.lock:
            self.turistiSulPonte-=1
            if self.turistiSulPonte==0:
                self.direzione=False
            self.conditionMonte.notifyAll() ?????????
            self.conditionMare.notifyAll()
    
    def releasePonteMonte(self):
        with self.lock:
            self.turistiSulPonte-=1
            if self.turistiSulPonte==0:
                self.direzione=True
            self.conditionMare.notifyAll() ??????
            self.conditionMonte.notifyAll()

            
class Montanaro(Thread):
    
    def __init__(self, i, p):
        super().__init__()
        self.id = i
        self.ponte = p 
        
    def run(self):
        while(True):
            print("Il montanaro %d chiede di attraversare." % self.id)
            self.ponte.acquirePonteMare()

            print("Il montanaro %d comincia ad attraversare." % self.id )
            sleep(1)
            self.ponte.setDirection(True)

            print("Il montanaro %d ha attraversato." % self.id)
            self.ponte.releasePonteMare()
            print("Il montanaro %d lascia il Ponte." % self.id)
            sleep(1)

        

class Marinaro(Thread):
    def __init__(self, i, p):
        super().__init__()
        self.id = i 
        self.ponte = p

    def run(self):
        while (True):
            print("Il marinaro %d chiede di attraversare." % self.id)
            self.ponte.acquirePonteMonte()

            print("Il marinaro %d comincia ad attraversare." % self.id)
            sleep(1)
            self.ponte.setDirection(False)

            print("Il marinaro %d ha attraversato." % self.id)
            self.ponte.releasePonteMonte()
            print("Il marinaro %d lascia il Ponte." % self.id)
            sleep(1)


ponte = Ponte()

marinari = [Marinaro(i, ponte) for i in range(0,5)]
montanari = [Montanaro(i, ponte)for i in range(0,5)]

for m in marinari:
    m.start()

for mon in montanari:
    mon.start()
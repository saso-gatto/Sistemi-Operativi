from threading import Thread, Lock, Condition
from time import sleep
from queue import Queue

class Negozio: 
    def __init__(self):
        self.slotPieni = 0
        self.ins = 0
        self.out=0
        self.dim = 10
        self.bufferClienti =  Queue()
        self.barbiereOccupato=False #?
        self.lock=Lock()
        self.conditionClienti = Condition(self.lock)
        self.conditionBarbiere = Condition(self.lock)

    def prossimoCliente(self): #Il barbiere verifica se nella coda ci sono clienti da gestire e li gestisce
                                #Va in wait se i clienti sono 0 --> il barbiere dorme
        with self.lock:
            while (self.bufferClienti.qsize()==0):
                self.conditionBarbiere.wait()
            #ilBarbiereSiSveglia
            print("il barbiere si è svegliato")
            self.conditionClienti.notifyAll()
            self.barbiereOccupato=True  
            prossimo = self.bufferClienti.get()
            self.barbiereOccupato=False
            print("Il prossimo cliente è: "+prossimo.getNome())
            return prossimo

            
    def aggiungiCliente(self,cliente):  #Metodo che gestisce l'aggiunta di nuovi clienti nella coda del negozio
                                #Se la coda è piena, il cliente se ne va scocciato
        with self.lock:
            if (self.bufferClienti.qsize()==self.dim):
                #il cliente se ne va
                print("Coda piena, cliente scocciato, scappa via altrove ...")
                return
            self.bufferClienti.put(cliente)
            if (self.barbiereOccupato):
                print("elementi posseduti "+str(self.bufferClienti.qsize())+" e barbiere occupato")
            else:
                print("elementi posseduti "+ str(self.bufferClienti.qsize())+" e barbiere libero")
            while (self.barbiereOccupato==True):
                self.conditionClienti.wait()
                print("sono in attesa perché massimo è occupato")
                #il cliente va in attesa nella condition
            self.conditionBarbiere.notifyAll()
            
            
                  
class Cliente(Thread):
    def __init__(self,nome,negozio):
        super().__init__() #richiamo del costruttore per gestire i thread     
        self.nome=nome
        self.negozio=negozio
    
    def getNome(self):
        return self.nome

    def run(self):
        daAggiungere = Cliente(self.getNome(), self.negozio)
        self.negozio.aggiungiCliente(daAggiungere)
        #print("sono nel run del cliente")
    

class Barbiere(Thread):
    def __init__(self,negozio):
        super().__init__() #richiamo del costruttore per gestire i thread
        self.negozio=negozio


    def run(self):
        while(True):
            print("Sono il barbiere.")
          #  cliente = Cliente (self.negozio.prossimoCliente().getNome(), self.negozio)
            self.negozio.prossimoCliente()
            print("Il barbiere ha gestito il cliente")
            sleep(0.5)

negozio = Negozio()
clienti = [Cliente] *10
for i in range (10):
    clienti[i] = Cliente (str(i),negozio)

massimo = Barbiere(negozio)
massimo.start()
print("Unica stringa probabilmente funzionante")
for i in range(10):
    clienti[i].start()


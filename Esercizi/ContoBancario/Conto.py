from threading import Thread,Lock,Condition
from time import sleep
from random import random,randint,randrange

class Transazione:
    def __init__(self,sorgente,dest,importo):
        self.sorgente=sorgente
        self.dest=dest
        self.importo=importo
        
class ContoBancario:
    def __init__(self,id,saldo):
        self.id=id
        self.saldo=saldo
        self.ultimeT = []    #massimo 50 però
        self.totTransazioni=0
        self.lock =Lock()
        self.occupata=False

    def setOccupata(self, condizione):
        if (condizione):
            self.occupata=True
        else:
            self.occupata=False
    
    def getOccupata (self):
        return self.occupata

    def getSaldo(self):
        with self.lock:
            return self.saldo

    def setSaldo(self,N):
        with self.lock:
            self.saldo=N

    def addTransazione (self,transazione):
        with self.lock:
            if (self.totTransazioni==50):
                self.ultimeT.pop(0)
                self.totTransazioni=0

            self.ultimeT.append(transazione)
            self.totTransazioni+=1
            self.occupata=False


class Banca:
    def __init__(self):
        self.conti = []
        self.lock = Lock()
        self.condition= Condition(self.lock)

    def aggiungiConto (self,conto):
        self.conti.append(conto)

    def find(self,t):
        try:
            if self.conti.index(t) >= 0:
                return True
        except(ValueError):
            return False

    def getSaldoConto(self,C): #utilizzare index per vedere se C è presente in conti
        with self.lock:
            return self.conti[C].getSaldo()
    
    def liberaConti(self,A,B):
        with self.lock:
            self.conti[A].setOccupata(False)
            self.conti[B].setOccupata(False)
            self.condition.notifyAll()

    def trasferisci (self,A,B,N):
        
        if (self.conti[A].getSaldo()<N):
            return False
        else:
            while (self.conti[A].occupata and self.conti[B].occupata):
                self.condition.wait()
            if (A<B):
                self.conti[A].setOccupata(True)
                self.conti[B].setOccupata(True)
            else:
                self.conti[B].setOccupata(True)
                self.conti[A].setOccupata(True)

            transazione = Transazione(A,B,N)
            saldoA=self.conti[A].getSaldo()
            saldoA-=N
            self.conti[A].setSaldo(saldoA)

            saldoB=self.conti[B].getSaldo()
            saldoB+=N
            self.conti[B].setSaldo(saldoB)

            self.conti[A].addTransazione(transazione)
            self.conti[B].addTransazione(transazione)
            self.liberaConti(A,B)
            return True


class Cliente(Thread):
    def __init__ (self,id,conto,banca):
        super().__init__()
        self.id=id
        self.conto=conto
        self.banca=banca

    def getConto(self):
        return self.conto

    def run(self):
        while True:
            daTrasferire = randrange(1000)
            destinatario = randrange (10) #id del destinatario
            #while (destinatario <= self.id)
            #   destinatario=randrange(10)
            
            print(f"Sono il cliente[{self.id}],saldo prima del trasferimento è: {self.conto.getSaldo()}, cliente destinario[{destinatario}], saldo destinatario: {self.banca.getSaldoConto(destinatario)}")
            if (self.banca.trasferisci(self.id,destinatario,daTrasferire)):
                print(f"Ho trasferito dal conto {self.id} al conto {destinatario} l'importo {daTrasferire}, saldo sorgente:{self.conto.getSaldo()},saldo destinatario: {self.banca.getSaldoConto(destinatario)}")
            else:
                print(f"Transazione saltata, non ho un saldo sufficiente")
            sleep(1)


def main():
    banca = Banca()
    totConti = 10
    clienti=[]
    for i in range(totConti):
        id = i
        conto = ContoBancario(id,1000)
        banca.aggiungiConto(conto)
        cliente = Cliente (id,conto,banca)
        clienti.append(cliente)
    for i in range (totConti):
        clienti[i].start()

if __name__ == "__main__":
    main()
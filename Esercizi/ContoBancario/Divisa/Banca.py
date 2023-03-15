from threading import Thread,Lock,Condition
from time import sleep
from random import random,randint,randrange
from ContoBancario import ContoBancario
from Transazione import Transazione

class Banca:
    def __init__(self):
        self.conti = []
        self.lock = Lock()
        self.condition= Condition(self.lock)

    def aggiungiConto (self,conto):
        self.conti.append(conto)

#   def find(self,t):
#       try:
#           if self.conti.index(t) >= 0:
#               return True
#        except(ValueError):
#            return False
#    def getSaldoConto(self,C): #utilizzare index per vedere se C è presente in conti
#        with self.lock:
#            while (find(C)==False):
#                self.condition.wait()
#            self.condition.notifyAll()
#            indice = self.conti.index(C)
#            return conti[indice].getSaldo()
    
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
            self.conti[A].setOccupata(True)
            self.conti[B].setOccupata(True)

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



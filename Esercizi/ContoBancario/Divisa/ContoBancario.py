from threading import Thread,Lock,Condition
from time import sleep
from random import random,randint,randrange
from Transazione import Transazione

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

from threading import Thread,Lock,Condition
from time import sleep
from random import randint, random
from enum import Enum
from queue import Queue #QUEUE:importa una coda di tipo fifo dalla classe queue

class TipoPizza(Enum):
	Margherita=1
	QuattroStagioni=2
	Americana=3
	Ortolana=4
	QuattroFormaggi=5


class Ordini:
    numeroCliente=0
    def __init__(self, codice, q): #da riguardare : RICORDA DI USARE PER ORA GENERAORDINE
        self.codice=codice
        self.q=q
        self.numeroCliente=self.numeroCliente+1
    
    def getQuantita():
        return self.q

    def getNumeroCliente():
        return self.numeroCliente



class Pizzaiolo(Thread):
    def __init__(self,nome,pizzeria):
        Thread.__init__(self)
        self.nome=nome
        self.pizzeria=pizzeria
    
    def run(self): #metodo che in teoria dovrebbe gestire il prelievo di un ordine da BO e l'inserimento nel buffer BP
        while (True):
            sleep(random()*2)
            ordine = self.pizzeria.getOrdine()
            print("Sono il pizzaiolo %s e ho l'ordine %s"%(self.getName(),ordine))
            sleep(random()*2)
            self.pizzeria.putPizza(ordine)


class Cliente (Thread):
    def __init__ (self,nome,pizzeria):           #buffer: è quello che sottomette l'ordine
        Thread.__init__(self)
        self.nome=nome
        self.pizzeria=pizzeria

    def run(self):
        while True:
            numeroPizze = 1 + randint(1,5)
            codicePizza = TipoPizza(randint(1,5))
            ordineCliente=self.pizzeria.putOrdine(codicePizza,numeroPizze)
            
            sleep(random()*2)
            self.pizzeria.getPizza(ordineCliente) #ricorda che in getPizza bisogna gestire l'identificativo dell'ordine

class codaPizze:
    
    def __init__(self):
        self.dim=10
        self.bufferPizza=[None] * self.dim
        self.ins= 0                 
        self.out= 0
        self.lock = Lock()                              #sto equipaggiando la queue di un lock
        self.full_condition = Condition (self.lock)
        self.empty_condition = Condition(self.lock)

    def aggiungiPizza(self,p):
        with self.lock:
            while (len(self.bufferPizza)==self.dim):
                self.full_condition.wait()
            self.empty_condition.notifyAll()
            self.bufferPizza[self.ins]=p
            self.ins = (self.ins+1) % len(self.bufferPizza)

    def ritiraPizza(self,numeroOrdine):
        with self.lock:
            while (len(self.bufferPizza)==0):
                self.empty_condition.wait()
            self.full_condition.notifyAll()
            for i in range (0,len(self.bufferPizza)):
                if self.bufferPizza.numeroOrdine== numeroOrdine:
                    self.out=i
            returnValue= self.bufferPizza[self.out]
            self.bufferPizza[self.out]=None
            return returnValue



class Pizzeria:

    codaPizze = codaPizze()
    bufferOrdine=Queue(10)

    def putOrdine (self,codicePizza,numeroPizze):
        ordine = Ordini(codicePizza,numeroPizze)
        self.bufferOrdine.put(ordine)
        return ordine

    def getOrdine (self):
        try:
            return self.bufferOrdine.get()
        finally:
            pass
        return None

    #il metodo putPizza riceve in input un ordine
    def putPizza (self,pizza):
        self.codaPizze.aggiungiPizza(pizza)

    #il metodo getPizza blocca il thread chiamante nel caso in cui l'ordine richiesto non sia stato servito
    def getPizza (self,ordine):
        self.codaPizze.ritiraPizza(ordine.getNumeroCliente())


def main():
    p = [Pizzaiolo] * 3
    c = [Cliente] * 10
    pizzeria = Pizzeria()

    for i in range(0, 3):
        p[i] = Pizzaiolo("Peppino_" + str(i), pizzeria)
        p[i].start()

    for i in range(0, 10):
        c[i] = Cliente("Melo_" + str(i), pizzeria)
        c[i].start()

if __name__ == '__main__':
    main()
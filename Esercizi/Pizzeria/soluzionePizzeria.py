from enum import Enum
from queue import Queue
from threading import RLock, Condition

import threading
from random import randint, random
import time

class TipoPizza(Enum):
    Margherita = 1
    QuattroStagioni = 2
    Capricciosa = 3


class Pizzaiolo(threading.Thread):
    def __init__(self, name, pizzeria):
        threading.Thread.__init__(self)
        super().setName(name)
        self.pizzeria = pizzeria

    def run(self):
        while True:
            try:
                print("Il pizzaiolo" + self.getName() + " verifica la presenza di una ordinazione...")
                ordine = self.pizzeria.getOrdine()

                tempoDiPreparazione = ordine.quantita

                print("Il pizzaiolo " + self.getName() + " ha prelevato l'ordine numero " + str(ordine.codiceOrdine) + " e prepara le pizze");

                time.sleep(tempoDiPreparazione * 1)
                ordine.prepara()

                print("Il pizzaiolo " + self.getName() + " ha preparato le pizze per l'ordine numero " + str(ordine.codiceOrdine))

                self.pizzeria.putPizze(ordine)
                #
                # Sigaretta...
                #
                time.sleep(randint(1,3))
            finally:
                pass



class Cliente(threading.Thread):
    def __init__(self, name, pizzeria):
        threading.Thread.__init__(self)
        self.setName(name)
        self.pizzeria = pizzeria

    def run(self):
        while True:
            try:
                numeroPizze = 1 + randint(0,7)
                codicePizza = TipoPizza(randint(1,3))

                print("Il cliente " + self.getName() + " entra in pizzeria e prova ad ordinare delle pizze")
                ordine = self.pizzeria.putOrdine(codicePizza, numeroPizze)
                print("Il cliente " + self.getName() + " aspetta le pizze con codice d'ordine numero " + str(ordine.codiceOrdine))

                time.sleep(randint(0, numeroPizze * 1))
                self.pizzeria.getPizze(ordine)

                print("Il cliente " + self.getName() + " ha preso le pizze con codice d'ordine numero " + str(ordine.codiceOrdine))
                print(ordine.pizze)
                #
                # Prima o poi mi tornerÃ  fame
                #
                time.sleep(randint(0, numeroPizze * 1))
            finally:
                pass



class BlockingSet(set):
    lock = RLock()
    condition = Condition(lock)

    tagliaMassima = 10
    def add(self, _T):
        self.lock.acquire()
        try:
            while len(self) == self.tagliaMassima:
                self.condition.wait()

            self.condition.notifyAll()
            return super().add(_T)
        finally:
            self.lock.release()

    def remove(self, _T):
        self.lock.acquire()
        try:
            retValue = _T in self
            while (not retValue):
                self.condition.wait()
                retValue = _T in self

            super().remove(_T)
            self.condition.notifyAll()
            return retValue
        finally:
            self.lock.release()

class Ordine:
    nextCodiceOrdine = 0

    def __init__(self, tipoPizza, quantita):
        self.tipoPizza = tipoPizza
        self.quantita = quantita
        self.codiceOrdine = Ordine.nextCodiceOrdine
        self.pizze = ""
        Ordine.nextCodiceOrdine += 1

    def prepara(self):
        for i in range(0,self.quantita):
            self.pizze += "(*)"


class Pizzeria:
    blockingQueue = Queue(10)
    blockingSet = BlockingSet()

    def getOrdine(self):
        try:
            return self.blockingQueue.get()
        finally:
          pass
        return None

    def getPizze(self, ordine):
        self.blockingSet.remove(ordine)

    def putOrdine(self, codicePizza, quantita):
        ordine = Ordine(codicePizza, quantita)
        try:
            self.blockingQueue.put(ordine)
        finally:
            pass
        return ordine

    def putPizze(self, ordine):
        self.blockingSet.add(ordine)




def main():
    p = [Pizzaiolo] * 3
    c = [Cliente] * 10
    pizzeria = Pizzeria()

    for i in range(0, 3):
        p[i] = Pizzaiolo("Totonno_" + str(i), pizzeria)
        p[i].start()

    for i in range(0, 10):
        c[i] = Cliente("Geppino_" + str(i), pizzeria)
        c[i].start()

if __name__ == '__main__':
    main()
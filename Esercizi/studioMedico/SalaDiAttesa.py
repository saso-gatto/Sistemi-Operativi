from threading import Thread, Lock, Condition
from queue import Queue
from Paziente import Paziente
from Medico import Medico
from Segretaria import Segretaria
import random

class SalaDiAttesa:
    def __init__(self):
        self.codaVisite = Queue()
        self.codaRicette = Queue()
        self.codaPrioritaria = Queue()
        
        self.lockVisita = Lock()
        self.lockRicetta=Lock()
        self.conditionVisita = Condition(self.lockVisita)

        self.conditionRicetta = Condition(self.lockRicetta)

    def prossimaVisita(self): #questo metodo verrà utilizzato dal medico per chiamare il prossimo cliente
        with self.lockVisita:
            while (self.codaVisite.empty()):
                self.conditionVisita.wait()
            return self.codaVisite.get()

    def prossimaRicetta(self): #metodo richiamato dalla segretaria per smaltire i clienti che vogliono delle ricette
        with self.lockRicetta:
            while (self.codaRicette.empty() and self.codaPrioritaria.empty()):
                self.conditionRicetta.wait()
            if (self.codaPrioritaria.empty()==False):
                return self.codaPrioritaria.get()
            elif (self.codaRicette.empty()==False):
                return self.codaRicette.get()

    def aggiungiVisita(self,p): #metodo richiamato dal paziente per potersi mettere in attesa per una prossima visita
        self.codaVisite.put(p)
        with self.lockVisita:
            self.conditionVisita.notifyAll()
            #avviso il dottore che sono in attesa?

    def aggiungiRicetta(self,p):
        self.codaRicette.put(p)
        with self.lockRicetta:
            print("sono in aggiungi ricetta")
            self.conditionRicetta.notifyAll()


def main():
    sala = SalaDiAttesa()
    med = Medico(sala)
    segretaria = Segretaria(sala)
    pazienti = [Paziente]*10
    for i in range(10):
        richiesta = random.randint(0,1)
        if (richiesta==1):
            print("voglio una ricetta")
        pazienti[i]=Paziente(i,sala,richiesta)

    med.start()
    segretaria.start()
    for i in range(10):
        pazienti[i].start()

if __name__ == '__main__':
    main()
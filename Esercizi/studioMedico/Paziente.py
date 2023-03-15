from threading import Thread
import random
class Paziente(Thread):
    def __init__(self,id,salaAttesa, richiesta):
        super().__init__()
        self.id=id
        self.sala=salaAttesa
        self.richiesta=richiesta

    def run(self):
        richiesta = random.randint(0,1)
        daAggiungere = Paziente(self.id,self.sala,self.richiesta)
        if (richiesta==0):
            print("Sono il paziente numero: "+str(self.id)+", ho bisogno di una visita medica")
            self.sala.aggiungiVisita(daAggiungere)
        elif (richiesta==1):
            print("Sono il paziente numero: "+str(self.id)+", ho bisogno della ricetta")
            self.sala.aggiungiRicetta(daAggiungere)


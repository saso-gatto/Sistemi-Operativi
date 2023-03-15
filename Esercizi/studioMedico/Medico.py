from threading import Thread
import random

class Medico(Thread):
    def __init__(self,sala):
        super().__init__()
        self.salaAttesa=sala

    def run(self):
        while (True):
            print("Sono il mededico, chiamo il prossimo paziente")
            paziente = self.salaAttesa.prossimaVisita()
            ricetta = random.randint(0,1)
            if (ricetta==0):
                print("Stai bene, puoi andare")
            elif (ricetta==1):
                print("Prescrivo la ricetta per il paziente")
                self.salaAttesa.aggiungiRicetta(paziente)
            

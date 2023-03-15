from threading import Thread

class Segretaria(Thread):
    def __init__(self,sala):
        super().__init__()
        self.salaAttesa=sala

    def run(self):
        while (True):
            print("Sono la segreteraia, chiamo il prossimo paziente")
            paziente = self.salaAttesa.prossimaRicetta()
            print("Prescrivo la ricetta per il paziente")

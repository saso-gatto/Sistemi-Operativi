from threading import Thread,Lock,Condition
from time import sleep
from random import random,randint,randrange
from Banca import Banca
from ContoBancario import ContoBancario


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
            #destinatario = randrange (10) #id del destinatario
            #while (destinatario <= self.id)
            #   destinatario=randrange(10)
            destinatario = randrange (10) #id del destinatario
            while (destinatario==self.id):
                destinatario = randrange (10)
            
            print(f"Sono il cliente[{self.id}], il mio saldo prima del trasferimento è: {self.conto.getSaldo()}")
            print(daTrasferire)
            if (self.banca.trasferisci(self.id,destinatario,daTrasferire)):
                print(f"Ho trasferito dal conto {self.id} al conto {destinatario} l'importo {daTrasferire}, saldo del conto sorgente:{self.conto.getSaldo()}")
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
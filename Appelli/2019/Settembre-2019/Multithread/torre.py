from threading import Thread,Lock,Condition
from time import sleep

class Torre:
    
    def __init__(self):
        pass
        
    def makeTorre(self,H: int, M : int, C : int):
        t = TorreInCostruzione(H)
        mattonatori = [Mattonatori(t) for _ in range (M)]
        cementatori = [Cementatori(t) for _ in range (C)]
        for m in mattonatori:
            m.start()
        for c in cementatori:
            c.start()
        
        t.attendiFine()
        t.stampaTorre()
        return t


class TorreInCostruzione:
    def __init__(self,H):
        self.torre = [" "]
        self.lock=Lock()
        self.condition=Condition(self.lock)
        self.torreFinita=Condition(self.lock)
        self.count=0
        self.strato=0
        self.ultimoPezzo="-"
        self.H=H

    def attendiFine(self):
        with self.lock:
            while (self.inCostruzione()==False):
                self.torreFinita.wait()

    def aggiungiPezzo(self, pezzo):
        with self.lock:
            while (self.ultimoPezzo!=pezzo and self.count<3):
                self.condition.wait()
            self.torre[self.strato]=self.torre[self.strato]+pezzo
            self.ultimoPezzo=pezzo
            self.count+=1
            #print(f'Count: {self.count}')

            if (self.count==3):
                self.count=0
                self.strato+=1
                self.torre.append("")
                if (self.ultimoPezzo=="-"):
                    self.ultimoPezzo="*"
                elif (self.ultimoPezzo=="*"):
                    self.ultimoPezzo="-"
                self.condition.notifyAll()
                #print("Strato nuovo")
                if (len(self.torre)==self.H):
                    print(f"sono nella condizione finale, h:{self.H}, len di torre: {len(self.torre)}")
                    self.torreFinita.notifyAll()
    
    def inCostruzione(self):
        if (self.strato<self.H):
            return True
        else:
            return False

    def stampaTorre(self):
        print(self.torre)


class Mattonatori(Thread):
    def __init__(self,torre):
        super().__init__()
        self.torre=torre
        self.pezzo="*"
    
    def run(self):
        while(self.torre.inCostruzione()):
            self.torre.aggiungiPezzo(self.pezzo)
            #sleep(1)

class Cementatori(Thread):
    def __init__(self,torre):
        super().__init__()
        self.torre=torre
        self.pezzo="-"

    def run(self):
        while(self.torre.inCostruzione()):
            self.torre.aggiungiPezzo(self.pezzo)
           # sleep(2)

torre=Torre()
torre.makeTorre(10,2,2)

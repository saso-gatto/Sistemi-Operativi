from threading import Thread,Lock
import random, time


class Striscia:
    def __init__(self):
        self.l=10
        self.striscia = []
        for i in range(0,self.l):
                self.striscia.append( ' ' )
        self.dirGatto=True #True vai a destra -- False a sinistra
        self.dirTopo=True
        self.trovato=False
        self.lock=Lock()
        self.gatto=random.randrange(0,self.l) #DA VEDERE
        self.topo=random.randrange(0,self.l)
        self.striscia[self.gatto]='*'
        self.striscia[self.topo]='.'


    def muoviGatto(self):
        self.lock.acquire()
        try:
            if (self.trovato==True):
                return True
            if(self.gatto==self.l-1 and self.dirGatto==True):
                self.dirGatto=False

            if(self.gatto==0 and self.dirGatto==False):
                self.dirGatto=True

            self.striscia[self.gatto]=" "

            if (self.dirGatto==True):
                self.gatto+=1
            else:
                self.gatto-=1

            if (self.gatto==self.topo):
                self.trovato=True
                self.striscia[self.gatto]="!"
                return True
            self.striscia[self.gatto]="*"
            return False
        finally:
            self.lock.release()

    def muoviTopo(self):
        self.lock.acquire()
        try:
            if (self.trovato==True):
                return True

            if(self.topo==self.l-1 and self.dirTopo==True):
                self.dirTopo=False

            if(self.topo==0 and self.dirTopo==False):
                self.dirTopo=True
            self.striscia[self.topo]=' '

            if (self.dirTopo==True):
                self.topo+=1
            else:
                self.topo-=1
                
            if (self.topo==self.gatto):
                self.trovato=True
                self.striscia[self.topo]="!"
                return True
            self.striscia[self.topo]="."
            return False
        finally:
            self.lock.release()


    def stampaStriscia(self):
        self.lock.acquire()
        try:
            for i in range(self.l):
                (''.join(self.striscia[i])) 
            return self.trovato
        finally:
            self.lock.release()

class Gatto(Thread):
    def __init__(self,s):
        Thread.__init__(self)
        self.striscia=s

    def run(self):
        print("I'am the cat")
        while (self.striscia.muoviGatto()==False):
            time.sleep(0.020)

class Topo(Thread):
    def __init__(self,s):
        Thread.__init__(self)
        self.striscia=s
    
    def run(self):
        print("I'am the mouse")
        while (self.striscia.muoviTopo()==False):
            time.sleep(0.020)


class Display(Thread):
    def __init__(self,s):
        Thread.__init__(self)
        self.striscia=s

    def run(self):
        print ("First run Display")
        while (not striscia.stampaStriscia()):
            time.sleep(0.020)

striscia = Striscia()
tom=Gatto (striscia)
jerry = Topo (striscia)
display = Display(striscia)
print("iniziamo")
display.start()
tom.start()
jerry.start()
time.sleep(10)
        

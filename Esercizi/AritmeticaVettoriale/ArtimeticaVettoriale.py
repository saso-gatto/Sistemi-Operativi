from threading import Thread, Condition, Lock
import math,time, multiprocessing

class Barrier:
    def __init__(self,n):
        self.soglia=n   # numero thread
        self.threadArrivati = 0
        self.lock = Lock()
        self.condition = Condition(self.lock)

    def wait(self):
        with self.lock:
            self.threadArrivati +=1
            if self.threadArrivati == self.soglia:
                self.condition.notifyAll()

            while self.threadArrivati < self.soglia:
                self.condition.wait()    


class OperazioniMultiThread(Thread):
    def __init__(self,minI,maxI,oper,b,v1,v2,v3):
        #self.numProc = multiprocessing.cpu_count()
        self.numProc = 4
        self.b=b
        self.v1=v1
        self.v2=v2
        self.v3 = v3 
        self.minI = minI
        self.maxI = maxI
        self.oper=oper #    true= somma       false= sottrai
        self.totale=0
    
    def getTotale(self):
        return self.totale

    def somma (self): #passare anche i valori di min e max distinti
        print(f"Test minI e maxI: {minI},{maxI} ")
        for i in range (self.minI,self.maxI):
            self.v3[i]=self.v1[i]+self.v2[i]
        self.b.wait()
        return self.v3

    def sottrai(self):
        for i in range (minI,maxI):
            v3[i]=v1[i]-v2[i]

class Operazioni:           #QUESTA È la classe giusta da finire
    def __init__(self,v1,v2):
        self.v1=v1
        self.v2=v2

    def somma(self):
        calcolatoreSomma = [None]*self.numProc
        min = 0
        max = len(self.v1)
        numProc = multiprocessing.cpu_count()
        ciucci = []
        fettina = len(self.v1)+1 //self.numProc
        b=Barrier(self.numProc+1)
        for i in range (self.numProc-1):
            minI=i*fettina
            maxI=minI+fettina-1
            ciucci.append(OperazioniMultiThread(minI,maxI,oper,b,v1,v2,v3))
            calcolatoreSomma[i].start()
        minI = self.numProc -1 * fettina
        maxI = len(self.v1)
        calcolatoreSomma[i]=Operazioni(self.minI,self.maxI,True,self.b,self.v1,self.v2,self.v3).somma
        calcolatoreSomma[self.numProc-1].start()
        b.wait()


class OperazioniMultiThread (Thread):
    def __init__(self,v1,v2,MinI,MaxI):
        Thread.__init__(self)
        self.v1=v1
        self.v2=v2 
        self.numProc=4
        self.b=Barrier(self.numProc+1)
        self.v3=[None]*len(v1)          #questo è il v3 su cui bisogna lavorare
        self.minI=MinI
        self.maxI=MaxI
        self.dim=len(self.v1)


    def sommaMultiThread(self):
        fettina = len(self.v1)+1 //self.numProc
        calcolatoreSomma = [None]*self.numProc
        b=Barrier(self.numProc+1)
        
        for i in range (self.numProc-1):
            minI=i*fettina
            maxI=minI+fettina-1
            calcolatoreSomma[i]=Operazioni(self.minI,self.maxI,True,self.b,self.v1,self.v2,self.v3).somma
            calcolatoreSomma[i].start()
        
        minI = self.numProc -1 * fettina
        maxI = len(self.v1)
        calcolatoreSomma[i]=Operazioni(self.minI,self.maxI,True,self.b,self.v1,self.v2,self.v3).somma
       # calcolatoreSomma[self.numProc-1].start()
        print(f"test: {calcolatoreSomma[0]}")
       # b.wait()
        return calcolatoreSomma

    def run(self):
        for i in range (self.dim):
            self.v3[i]+=self.calcolatoreSomma[i]



v1 = [10,12,17,4,2,2,2,2,9,12]
v2 = [8,1,5,2,1,1,1,1,4,5]

if len(v1) != len(v2):
    print(f"Dimensione vettori diversa")

test =[None]*len(v1)
op = OperazioniMultiThread(v1,v2,0,len(v1))
test= op.sommaMultiThread()

for i in range(len(test)):
    print(test[i])


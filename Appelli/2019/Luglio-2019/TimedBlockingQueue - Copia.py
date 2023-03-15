from threading import Thread,Lock,Condition
from time import sleep
from random import random

class TimedBlockingQueue:
    def __init__(self,dim):
        self.dim=dim
        self.buffer=[]
        self.lock=Lock()
        self.full_condition=Condition(self.lock)
        self.empty_condition=Condition(self.lock)

        self.daRimuovere=-1
        self.time=-1

    def put(self,elem):
        with self.lock:
            while (len(self.buffer)==self.dim):
                self.full_condition.wait()
            self.buffer.append(elem)
            self.empty_condition.notifyAll()


    def get(self):
        with self.lock:
            while (len(self.buffer)==0):
                self.empty_condition.wait()
            self.full_condition.notifyAll()
            return self.buffer.pop()

    def timedPut(self,elem, timeout):
        with self.lock:
            while (self.dim==len(self.buffer)):
                self.full_condition.wait()
            self.empty_condition.notifyAll()
            self.buffer.append(elem)
            self.daRimuovere=elem
            self.time=timeout

    def waitFor(self,e):
        with self.lock:
            if (e not in self.buffer):
                print("Elemento non presente \n")
                return False
            while (e in self.buffer or self.time!=0):
                self.condition.wait()
            if (self.time==0):
                self.time=-1
                self.daRimuovere=-1
                return False
            else:
                self.time=-1
                self.daRimuovere=-1
                return True

class Scadenza(Thread):


class Timer (Thread):
    def __init__ (self,queue,id):
        self.queue = queue
        Thread.__init__(self)
        self.id=id
        self.caso= randint( 0 , 3 )

    def run(self):
        while (True):
            if (caso==0):               #PUT
                elem=randint(0,100)
                self.queue.put(elem)
            if (caso==1):               #GET
                elem= self.queue.get()
                print(f"Sono il thread {self.id}, faccio la get: {elem}")
            if (caso==2):               #TIMED PUT
                elem=randint(0,100)
                time=random.random(0,10)
                self.queue.timedPut(elem,time)
            if (caso==3):
                

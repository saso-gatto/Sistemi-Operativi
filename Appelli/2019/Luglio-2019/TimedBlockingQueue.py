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
        self.time_condition = Condition(self.lock)
        self.bufferTemp = []
        


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
            temp = self.buffer.pop()
            self.full_condition.notifyAll()
            self.time_condition.notifyAll()
            return temp

    def timedPut(self,elem, timeout):
        with self.lock:
            self.put(elem)
            temp = Scadenza(self, elem,timeout)
            temp.start()


    def waitFor(self,e):
        with self.lock:
            if (e not in self.buffer):
                print("L'elemento e non è presente")
                return False
            else:
                while (e in self.buffer):
                    self.time_condition.wait()
                if (e in self.bufferTemp):                  #e è stato rimosso per scadenza di tempo
                    self.bufferTemp.remove(e)
                    return False
                else:                                       
                    return True


    def rimuoviElemento(self, e):
        with self.lock:
            if (e in self.buffer):
                if (len(self.buffer)==self.dim):
                    self.full_condition.notifyAll()
                self.buffer.remove(e)
                self.bufferTemp.append(e) #e viene salvato in un buffer dove vi sono elementi con il tempo scaduto
                self.time_condition.notifyAll()
                return True
            else:
                return False

        

class Scadenza(Thread):
    def __init__ (self,queue,elem,timeout):
        self.queue = queue
        Thread.__init__(self)
        self.elem=elem
        self.timeout=timeout
    
    def run(self):
        time.sleep(self.timeout)        #Eseguo il thread, scaduto il tempo si occuperà di rimuovere l'elemento dalla coda
        if  (self.queue.rimuoviElemento(self.elem)==True):
            print ("elemento rimosso")
        



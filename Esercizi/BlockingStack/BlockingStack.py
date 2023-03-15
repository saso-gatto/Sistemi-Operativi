from threading import Thread,Lock,Condition


#Strtutura dati che si comporta come LIFO
class BlockingStack:

    def __init__ (self,dim):
        self.dim = dim
        self.buffer = []
        self.lock= Lock()
        self.full_condition= Condition (self.lock)
        self.empty_condition= Condition (self.lock)
    
    def put (self,elemento):
        with self.lock:
            while (self.dim==len(self.buffer)):
                self.full_condition.wait()
            self.empty_condition.notifyAll()
            self.buffer.append(elemento)

    def take (self):
        with self.lock:
            while (len(self.buffer)==0):
                self.empty_condition.wait()
            self.full_condition.notifyAll()
            return self.buffer.pop()

    def trovato(self,elemento):
        try:
            if self.buffer.index(elemento)>=0:
                return True
        except(ValueError):
            return False

    def takeElemento (self,elemento):
        with self.lock:
            while (self.trovato(elemento)==False):
                self.empty_condition.wait()
            self.full_condition.notifyAll()
            self.buffer.remove(elemento)
            return elemento

buffer = BlockingStack(10)
buffer.put(1)
buffer.put(43)
buffer.put(17)
buffer.put(25)

print(buffer.takeElemento(43))
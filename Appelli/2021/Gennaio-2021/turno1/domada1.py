Aggiungo al costruttore:    self.oldshit=0
                            self.condition = Condition(self.lock)

Aggiungo al metodo shift, dopo riga 69: self.condition.notifyAll()



def oldget (self, i:int, d:int):
    with self.lock:
        self.oldshift=self.shiftAttuale
        while (((d==0 and self.Out[self._om(i)]==0) or (d==1 and self.In[i]==0)) and (self.oldshift!=shiftAttuale)):
            self.condition.wait()
        if (d==0):
            return  self.Out[self._om(i)]
        elif (d==1):
            return self.In[i]
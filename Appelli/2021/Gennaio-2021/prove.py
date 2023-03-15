#Data un intero N, verificare che non ci siano almeno size/2 elementi i-esmi (quindi sia In[i] che Out[_om(i)] 
#che siano entrambi 0.
#Se ci sono, resettare tali elementi.

Aggiungo al costruttore: 
self.soglia=self.size/2

def check(self):
    self.cont=0
    with self.lock:
        for i in range (0,self.soglia):
            if (self.In[i]==0 && self.Out[_om(i)]):
                self.cont++
        if (self.cont>=self.soglia):
            return True
        else:
            return False
    

def resetElementi(self):
    with self.lock:
        for i in range (0,self.soglia):
            if (self.In[i]==0 && self.Out[_om(i)]):
                self.nuovoValore = randrange(0,self.size())
                self.In[i]=self.nuovoValore
                self.Out[_om(i)]


# Modifica i metodi presenti nel materiale impedendo che due thread possano modificare (sia set che get)
# consecutivamente lo stesso indice. Sblocca tale thread quando ne entra uno che richiama un i diverso.

Aggiungo al costruttore  --  : self.ultimoId, self.condition = Condition(self.lock)  --

Aggiungo al metodo set tra riga 72 e 73
if (self.i!=self.ultimoId):
    self.condition.notifyAll()
while (self.i==self.ultimoId):
    self.condition.wait()
self.ultimoId=self.i



# Aggiungere un metodo waitForSet (i: int, v: int, d: int, w : int)
# Il thread rimane in attesa bloccante finché non viene fatto un set del valore passato (w)
Aggiungo al costruttore: 
condition = Condition(self.lock)
self.w=-1

def impostaVarWait (self, w):
    with self.lock:
        self.w=w

def waitForSet(self, i: int, v: int, d:int):
    with self.lock:
        if (self.w==-1):
            self.set(i,v,d) #setta il valore normalmente
        while (v!=self.w and self.w!=-1):
            self.condition.wait()
        self.w=-1
        self.set(i,v,d)


def set(self, i : int, v : int, d : int):
    with self.lock:
        if self.w!=-1 and v!=self.w:
            self.waitForSet(i,v,d)
        elif self.w!=-1 and v==self.w:
            self.condition.notifyAll()
         
        if d == 0 :
            self.Out[self._om(i)] = v
        else:
            self.In[i] = v
        if self.In[i] == self.Out[self._om(i)]:
            self.In[i] = 0
            self.Out[self._om(i)] = 0
        elif v != 0:
            self.waitCondition.notifyAll()



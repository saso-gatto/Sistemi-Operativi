Aggiungo al costruttore:    self.threadVincitore=-1
                            self.attendiCond=Condition(self.lock)

Nel metodo gioco, prima della riga 37:  self.threadVincitore=self.giocate.get(k)
                                        self.attendiCond.notifyAll()

def puntaNumero (self,n:int):
    with self.lock:
        self.giocate.setdefault(n[]).append(current_thread().ident)
        self.ngiocate+=1
        self.threadGioca.notify()
        while (!self.partitaInCorso): #self.threadVincitore!=-1
            self.attendiCond.wait()
        if (self.threadVincitore==self.current_thread().ident):
            self.threadVincitore=-1
            return True
        else:
            return False


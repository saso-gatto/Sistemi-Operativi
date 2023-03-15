Aggiungo al costruttore:    self.numScrittori=0
                            self.tcond=Condition(self.lock)
                            self.prioritaScrittore=False

def acquireTLock(self):
    while (self.numLettori>3 or self.numScrittori>=2 or self.prioritaScrittore):
        self.tcond.wait()

def releaseTLock(self):
    with self.lock:
        self.prioritaScrittore=True
        self.condition.notifyAll()

Modifica acquireReadLock:
                         modifca condizione while: while (self.prioritaScrittore or (​self​.numScrittoriInAttesa > ​0​​
                                                          and​​   self​.numGiriSenzaScrittori > ​self​.SOGLIAGIRI) 
                                                          or self.ceUnoScrittore):
                         prima del release: self.numScrittori=0
                                self.tcond.notifyAll()

Modofica relaseReadLock:
                        prima di "if numLettori==0": if numLettori<3:
                                                        self.tcond.notifyAll()

Modfica acquireWriteLock:
                        prima del release:
                                        self.numScrittori+=1

Modifica releaseWriteLock:
                        self.prioritaScrittore=False
                        self.tcond.notifyAll()
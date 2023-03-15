aggiungo al costruttutore: self.conditionT = Condition(Lock)
aggiungo al costruttutore: self.prioritaScrittore=False  --- lo pongo a 0 quando l ultimo dei possessori dei tlock esce ,numTLock = 0


def acquireTLock (self):
    while (self.numLettori>3 || (self.numGiriSenzaScrittore=0 && self.ceUnoScrittore) || self.prioritaScrittore):
        self.conditionT.wait()
    self.numTLock+=1


def relaseTLock(self):
    with self.lock:
        self.prioritaScrittore=True
        self.numTLock-=1

Modifica del while del metodo acquireReadLock(self): 

while self .ceUnoScrittore or 
( self .numScrittoriInAttesa > 0 and self .numGiriSenzaScrittori > self .SOGLIAGIRI) || self.PrioritaScrittore:

Modifica del release di WriteLock.
Aggiunta del rigo di codice: self.prioritaScrittore=False

Aggiunta nel metodo del releaseReadLock(self), dopo la riga "self.numLettori-=1";
if (self.numLettori<3):
    self.conditionT.notifyAll()

Aggiunta nel metodo releaseWriteLock(self), dopo la riga self.ceUnoScrittore=False --> self.conditionT.notifyAll

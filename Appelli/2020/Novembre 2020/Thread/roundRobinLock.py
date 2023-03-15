Aggiungo al costruttore: self.oldTurno=-1
                         self.attesaPresidente=0
                         self.idPresidente=0

def setPresident (self, id: int):
    with self.lock:
        self.idPresidente=id

def urgentAcquire (self):
    with self.lock:
        self.attesaPresidente+=1
        while (self.possessori>0 and self.turnoCorrente!= self.idPresidente):
            self.conditions[self.idPresidente].wait()
        self.attesaPresidente-=1
        self.oldTurno=self.turnoAttuale
        self.possessori+=1

Modfica della condizione del while dell acquire, rigo 23
while (self.possessori>0 and (self.turnoCorrente!=id or self.turnoCorrente!=idPresidente)):


Modifica del release, prima del rigo 35:
if (self.oldTurno!=-1 and self.turnoAttuale=self.idPresidente):
    self.turnoAttuale=self.oldTurno
    self.oldTurno=-1
    self.conditions[self.turnoAttuale].notifyAll()
elif self.possessori == 0  and self.inAttesa[self.turnoCorrente] ==0:
Questo if riprende il corpo dell if del rigo 35.


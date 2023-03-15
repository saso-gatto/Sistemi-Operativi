from threading import Thread,RLock,Condition

class Sede:
    def __init__(self,N):
        self.uffici =[]
        self.ultimiTicket = [] # qui salvo gli ultimi 5 ticket per il display
        self.lock = Lock()
        self.conditionSede = Condition(self.lock)
        for (i in range("ABCDEFGHILMNOPQRSTUVZ")):
            ufficio[i]=Ufficio(i)
        self.stampaUltimi=True

    #rilascia il prossimo ticket disponibile per uff.
    #Restituisce una stringa contenente il codice del ticket rilasciato.
    def prendiTicket(uff): 
        return self.uffici[uff].assegnaTicket()

    #chiama il prossimo ticket non ancora servito per uff.
    #il display deve essere aggiornato in accordo
    #si pone in attesa bloccante se il prossimo ticket da chiamare non è stato ancora rilasciato
    def chiamaTicket(uff):  
        ultimo=self.uffici[uff].chiamaProssimoTicket()
        with self.lock:
            if (len(self.ultimiTicket)==5):
                self.ultimiTicket.pop()
            self.ultimiTicket.insert(0,self.ultimo)
            self.conditionSede.notify_all()
            return ultimo

    def presente(self,ticket):
        for i in range len(self.ultimiTicket):
            if (ticket ==self.ultimiTicket[i]):
                return True
        return False

    #metodo che si mette in attesa che il ticket identificato da "ticket" venga chiamato
    #esce quando ticket viene chiamato o quando risulta fra gli ultimi 5 del display
    def waitForTicket(ticket):
        with self.lock:
            while (self.presente(ticket)==False):
                self.conditionSede.wait()

    #interrrompe la visual. del display e mostra  a video gli utenti in attesa per ogni ufficio.
    def printAttese():
        with self.lock:
            self.stampaUltimi=False
            for (i in range len(self.uffici)):
                self.uffici[i].stampaTicket
            self.stampaUltimi=True

    def getStampaUltimi(self):
        return self.stampaUltimi

    def getUltimiTicket:
        with self.lock:
            return self.ultimiTicket

class Ufficio:
    def __init__(self,l):
        self.id=0
        self.lettera=l
        self.ticketPrenotati=[]
        self.lock=Lock()
        self.condition=Condition(lock)
        
    def creaTicket(self):
        ticket=self.lettera
        if (self.id>99):
            ticket.append("% s" % self.id )
        elif (self.id<100 and self.id>9):
            ticket.append("0")
            ticket.append("% s" % self.id)
        elif (self.id<10)
            ticket.append("00")
            ticket.append("% s" % self.id )
        return ticket 

    def assegnaTicket(self):
        with self.lock:
            ticket=self.creaTicket()
            self.ticketPrenotati.append(ticket)
            self.condition.notify_all()

    def chiamaProssimoTicket(self):
        with self.lock:
            while (len(self.ticketPrenotati)==0):
                self.condition.wait()
            return self.ticketPrenotati.pop()

    def stampaTicket(self):
        with self.lock:
            for i in range (len(self.ticketPrenotati)):
                print(self.ticketPrenotati[i])

class Display(Thread):
    def __init__(self, sede):
        super().__init__()
        self.sede=sede
        self.lock=Lock()

    def run(self):
        while (self.sede.stampaUltimi()==True):
            ultimi = self.sede.getUltimiTicket()
            for (i in range 5):
                print(ultimi[i])

class Persona(Thread):
    def __init__(self, sede):
        Thread.__init__(self)
        self.sede = sede
        self.n = len(sede.uffici)

    def run(self):
        while True:
            ticket = self.sede.prendiTicket(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ"[0:self.n]))
            self.sede.waitForTicket(str(ticket))


class Impiegato(Thread):
    def __init__(self, sede, lettera):
        Thread.__init__(self)
        self.sede = sede
        self.ufficio = lettera
 
    def run(self):
        while True:
            self.sede.chiamaTicket(self.ufficio)
            time.sleep(random.randint(0,4))
            #
            # Notifica di voler stampare il riepilogo attese 
            #
            if random.randint(0,5) >= 4:
                self.sede.printAttese()
from threading import Thread,Lock,Condition
from time import sleep

class PivotBlockingQueue:
    def __init__(self, n):
        self.pivot = -1
        self.dim = n
        self.buffer = []
        self.lock = Lock()
        self.condition = Condition (self.lock)
        self.criterio=True
    
    # METODO TAKE
    # individua l’elemento PIVOT e lo elimina dalla coda; quindi estrae e restituisce un elemento
    # secondo il consueto ordine FIFO. Il metodo si pone in attesa bloccante se non sono presenti
    # nella coda almeno due elementi.

    def take(self):
        with self.lock:
            while (len(self.buffer)<2):
                self.condition.wait()
            if (self.criterio):
                self.setCriterioPivot(False)
            else:
                self.setCriterioPivot(True)
            self.rimuoviPivot()
            return self.buffer.pop()
    

    # METODO PUT
    # inserisce l’elemento T nella Blocking Queue. Se la coda contiene già N elementi, individua ed
    # elimina l’elemento PIVOT, quindi inserisce subito l’elemento T.
    
    def put (self, T:int):
        with self.lock:
            if (len(self.buffer)==self.dim):
                self.rimuoviPivot()
            self.buffer.append(T)
            self.condition.notifyAll()

    # CRITERIO PIVOT
    # Se minMax = True , al termine della chiamata il criterio di scelta dell’elemento PIVOT
    # diventerà quello del minimo elemento tra quelli presenti nella coda. 
    # Se minMax = False, al termine della chiamata il criterio di scelta dell’elemento PIVOT diventerà quello
    # del massimo elemento tra quelli presenti.
    # Se ci sono più di un valore massimo (o più di un valore minimo), 
    # deve essere selezionato l’elemento inserito più recentemente. 
    # Inizialmente il criterio di scelta dell’elemento PIVOT deve essere impostato su quello del minimo elemento.
    def setCriterioPivot (self, minMax: boolean):
        with self.lock:
            self.criterio = minMax

    def rimuoviPivot (self):
        with self.lock:
            pivot=self.buffer[0]
            for i in range (self.buffer):
                if (self.criterio and self.buffer[i]<=pivot):
                    pivot=self.buffer[i]
                elif (!self.criterio and self.buffer[i]>=pivot):
                    pivot=self.buffer[i]
            self.buffer.remove(pivot)
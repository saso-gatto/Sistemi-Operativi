class Cittadino:
    def __init__(self):
        self.soldiPercepiti = 0
        self.offerteRicevute = List()
        self.disoccupato = True
    
    def offriLavoro(self, nomeLavoro : str):
        #
        # Offre un lavoro a Self. Registra l'offerta nomeLavoro 
        # in self.offerteRicevute, ma solo se disoccupato = True
        # 
        pass
        
    def accettaLavoro(self,nomeLavoro : str):
        #
        # se nomeLavoro appartiene a self.offerteRicevute, pone self.disoccupato = False
        #
        pass
        
    def paga(self):
        #
        # Eroga 780 EUR a self, ma solo 
        # se quest'ultimo è disoccupato e il numero di offerte ricevute non supera 3
        # incrementa soldiPercepiti in accordo
        #
        pass
        
    def getPercepito(self):
        #
        # Restituisce quanto percepito finora
        #
        pass
        
class Popolo:        
    
    def __init__ (self):
        self.soldiErogati = 0
        self.soldiDisponibili = 1000000000
        self.cittadini = List()
        
    def distribuisciReddito(self):
        #
        # Attribuisce a tutti i componenti di self.cittadini il reddito del mese corrente (780 EUR a testa), 
        # decrementando
        # soldiDisponibili e incrementando soldiErogati. Genera una eccezione e interrompe l'operazione 
        # se 
        # durante l'operazione i soldiDisponibili dovessero finire
        #
        pass

    def aggiungiSoldi(self, valore : int):
        #
        # incrementa self.soldiDisponibili dell'ammontare di 'valore'
        #
        pass

    def iContiTornano(self):
        #
        # Verifica che la somma di quanto percepito dai singoli elementi di self.cittadini corrisponda a self.soldiErogati
        # restituisce un valore booleano in accordo
        #
        pass

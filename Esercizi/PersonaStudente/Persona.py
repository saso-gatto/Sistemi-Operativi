class Persona:
	def __init__(self,**kwargs): #kwargs:mappa chiave-valore, def__init__ indica il costruttore della classe
		if 'cf' in kwargs: #Se dentro questa mappa trovi la chiave cf, allora l'assegni al codice fiscale
			self.cf=kwargs['cf']
		if 'nome' in kwargs:
			self.nome=kwargs['nome']
		if 'cognome' in kwargs:
			self.cognome = kwargs['cognome']
		if 'eta' in kwargs:
			self.eta=kwargs['eta']
		
	#"kwargs" means "keyword arguments, è una mappa dove assegno determinati tipi di valore
	#non ci possono essere più di un costruttore
	#def __init__(self,cf,nome,cognome,eta):
	#	self.cf=cf
	#	self.nome=nome
	#	self.cognome=cognome
	#	self.eta=eta

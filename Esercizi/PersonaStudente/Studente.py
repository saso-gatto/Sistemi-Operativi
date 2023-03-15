from Persona import Persona

class Studente (Persona): #Possiamo ereditare anche altre classi
	listaEsami=[Esame(SOR,21,12), ESAME (ING,30,6)]
	def __init__(self, **kwargs):
		if 'matricola' in kwargs:
			self.matricola=kwargs['matricola']
		super().__init__(**kwargs) #Passiamo gli altri dati di persona
		#super(Studente, self).__init__(**kwargs)

	def print(self):
		super().print()
		print("Matricola: %s" % (self.matricola))

	def calcolaMedia (self):
		sommaCFU=0
		numeratore=0
		for e in self.listaEsami:
			sommaCFU+=e.cfu
			numeratore+=e.voto*e.cfu
			

	def controllaEsame (self):
		pass	

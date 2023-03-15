class Esame:
	def __init__(self,nome, cfu,voto=0):
		self.nome=nome
		self.cfu=cfu
		self.voto=voto

	def print(self):
		print ("Nome: %s \nvoto: &d\nCFU: %d" %(self.nome,self.voto,self.cfu))

	def __eq__(self,other): #definizione operatore equal ==
		return (self.nome==other.nome,) and (self.cfu==other.cfu)

	def __ne__(self,other):
		return not (self==other)

	

import datetime

class Plante :

	# TODO afficher arrosage et ajustement taille lampe

	def __init__(self, name):

		# We declare all variables we need for printing
		self.Name = name
		self.state = 1
		self.Pot = None
		self.T = None 
		self.Lampe = None
		self.Lampe_HPS = None 
		self.Lampe_puissance = None
		self.Engrais = None
		self.Engrais_freq = None
		self.Engrais_quantite = None
		self.Taille = None
		self.Floraison = None
		self.Floraison_début = None
		self.Rempoter = 0
		self.Arrosage_last = None

	def getName(self):
		return self.Name




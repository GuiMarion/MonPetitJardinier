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



	def Arrosage(self):

		if (self.Arrosage_last - datetime.datetime.now()).days > 3:
			print("Il est temps d'arroser, pour cela remplissez lentement le pot d'eau. Il faut qu'après\
			l'arrosage le pot soit beaucoup plus lourd qu'avant, 3 litres devraient suffirent.")

		if self.Engrais:
			print("Vous devraient aussi mettre de l'engrais, pour cela ajouter ", self.Engrais_quantite, "par litre d'eau.")

		self.Arrosage_last = datetime.datetime.now()




	def A1(self, interface, reponse):
		print("a1")
		if (reponse == None) :
			# Acquisition pot/terre
			interface.acquisition("Bonjour, vous avez decidez de planter une plante avec notre logiciel, bravo ! \
				Nous avons tout d'abord besoin d'une information, voulez-vous planter en pot ou en terre ?",["p","t"], [[self, "A1", [interface, "p"]], [self, "A1", [interface, "t"]]])

		else :
			self.Pot = reponse
			self.state = 2
			self.A2(interface)

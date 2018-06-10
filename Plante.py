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
		self.Taille = 0
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




	def A1(self, interface, reponse=None):
		if (reponse == None) :
			# Acquisition pot/terre
			interface.acquisition("Bonjour, vous avez decidé de planter une plante avec notre logiciel, bravo ! \
				Nous avons tout d'abord besoin d'une information, voulez-vous planter en pot ou en terre ?",["p","t"], [[self, "A1", [interface, "p"]], [self, "A1", [interface, "t"]]])

		else :
			self.Pot = reponse
			self.A2(interface)
			if self.state == 1 :
				self.state = 2



	def A2(self, interface):
		# Procédure germination
		if self.Pot:
				interface.acquisition("Vous avez choisi de panter en pot, c'est une très bonne idée. Pour cela \
					nous vous conseillons de mettre vos graines dans du coton humide pour les faire \
					germer. Revenez nous voir une fois fait.",["ok"], [[self, "A3", interface]])
		else :
				interface.acquisition("Vous evez choisi de planter en terre, c'est une très bonne idée. Pour cela \
					nous vous conseillons de mettre vos graines directement dans la terre. Revenez nous voir \
					une fois une pousse sortie de la terre.",["ok"], [[self, "A3", interface]])



	def A3(self, interface, reponse=None):
		# Acquisition germination
		if self.state == 2 :
			self.state = 3
		if self.Pot:
			if reponse == None :
				interface.acquisition("Votre graine a-t-elle germée ? Si c'est le cas un germe à du sortir. "
				, ["oui", "non"], [[self, "A4", interface], [self, "A3", [interface, "non"]]])

			if reponse == "non" :
				interface.acquisition("Revenez vers nous une fois qu'elle aura germée."
				,["ok"], [[self, "A4", interface]])



	def A4(self, interface):
		# Procédure pour mettre la graine en terre (cas Pot = 1)
		if self.state == 3 :
			self.state = 4
		interface.acquisition("Pour continuer, vous devez saisir délicatement la graine avec une pince à épiler que vous aurez\
			préalablement désinfectée et la déposer dans le pot dans lequel vous aurez fait un trou de 3 cm de profondeur\
			( un demi-doigt). La graine sera introduite avec le germe vers le bas, vous reboucherez ensuite sans trop tasser.",["ok"], [[self, "A5", [interface, None]]])


	def A6(self, interface, reponse=None):
		# Acquisition engrais
		if self.state == 5 :
			self.state = 6

		if reponse == None :
			interface.acquisition("Voulez-vous utiliser des engrais ? ",["oui", "non"], [[self, "A6", [interface, "oui"]], [self, "A6", [interface, "non"]]])

		if reponse == "oui" or reponse == "non" :
			self.Engrais = (reponse == 'oui')

		if self.Engrais:
			if reponse == 1 or reponse == 2 :
				self.Engrais_freq = int(reponse)
				self.A7(interface)

			else :
				interface.elmt_afficher = []
				interface.boutons = []
				interface.printT(25, 20, 100, "Quelle est la quantité à mettre dans un litre ? (en mL) ? Cette information devrait se situer derriere \
				la bouteille.")
				rep = interface.input(200, 200)
				self.Engrais_quantite = int(rep)

				interface.acquisition("Quelle est la fréquence d'utilisation de l'engrais ? (1 pour à chaque arrosage, 2 pour \
					un arrosage pour deux.",["1", "2"], [[self, "A6", [interface, 1]], [self, "A6", [interface, 2]]])

		if self.Engrais == False :
			self.A7(interface)


def A8(self):
	# Acquisition taille
	if self.state == 7 :
		self.state =  8

	print("Quelle est la taille de votre plante ? (en cm)")
	rep = interface.input(200, 200)
	self.Taille = int(rep)

	self.A9()



def A11(self):
	if self.state == 10 :
		self.state = 11
	interface.acquisition("felicitation, au cours de ces quelques mois vous avez appris beaucoup sur le jardinage."
		, ["ok"], [[interface, "accueil"]])

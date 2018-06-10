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
		self.Engrais_last = False
		self.Taille = 0
		self.Floraison = None
		self.Floraison_début = None
		self.Rempoter = 0
		self.Arrosage_last = datetime.datetime.now().day
		self.Arrosage_freq = 1

	def getName(self):
		return self.Name



	def Arrosage(self, interface):

		if (self.Arrosage_last - datetime.datetime.now().day) > self.Arrosage_freq:
			self.Arrosage_last = datetime.datetime.now().day

			if not self.Engrais :
				interface.acquisition("Il est temps d'arroser, votre plante pour cela remplissez lentement le pot d'eau. \
				Il faut qu'après l'arrosage le pot soit beaucoup plus lourd qu'avant, 3 litres devraient suffir."
					,["ok"], [[interface, "retour_arriere"]])

			elif not self.Engrais_last:
				interface.acquisition("Il est temps d'arroser, votre plante pour cela remplissez lentement le pot d'eau. \
				Il faut qu'après l'arrosage le pot soit beaucoup plus lourd qu'avant, 3 litres devraient suffir. Vous devrez aussi mettre \
				 de l'engrais, pour cela ajouter ", self.Engrais_quantite, "par litre d'eau.")
				self.Engrais_last = True

			else:
				interface.acquisition("Il est temps d'arroser, votre plante pour cela remplissez lentement le pot d'eau. \
				Il faut qu'après l'arrosage le pot soit beaucoup plus lourd qu'avant, 3 litres devraient suffir."
					,["ok"], [[interface, "retour_arriere"]])
				self.Engrais_last = False

	def A1(self, interface, reponse=None):
		if (reponse == None) :
			# Acquisition pot/terre
			interface.acquisition("Bonjour, vous avez decidé de planter une plante avec notre logiciel, bravo ! \
				Nous avons tout d'abord besoin d'une information, voulez-vous planter en pot ou en terre ?"
				,["Pot","Terre"], [[self, "A1", [interface, "p"]], [self, "A1", [interface, "t"]]])

		else :
			self.Pot = reponse
			self.A2(interface)
			if self.state == 1 :
				self.state = 2



	def A2(self, interface):
		# Procédure germination
		if self.Pot:
				interface.acquisition("Vous avez choisi de planter en pot, c'est une très bonne idée. Pour cela \
					nous vous conseillons de mettre vos graines dans du coton humide pour les faire \
					germer. Revenez nous voir une fois fait.",["ok"], [[self, "A3", interface]])
		else :
				interface.acquisition("Vous avez choisi de planter en terre, c'est une très bonne idée. Pour cela \
					nous vous conseillons de mettre vos graines directement dans la terre. Revenez nous voir \
					une fois une pousse sortie de la terre.",["ok"], [[self, "A3", interface]])



	def A3(self, interface, reponse=None):
		# Acquisition germination
		if self.state == 2 :
			self.state = 3
		if self.Pot:
			if reponse == None :
				interface.acquisition("Votre graine a-t-elle <def =un germe est une petite tige qui sort de la graine>germée</def> ? "
				, ["Oui", "Non"], [[self, "A4", interface], [self, "A3", [interface, "non"]]])

			if reponse == "non" :
				self.state == 2
				interface.acquisition("Revenez vers nous une fois qu'elle aura germée."
				,["ok"], [[interface, "accueil"]])



	def A4(self, interface):
		# Procédure pour mettre la graine en terre (cas Pot = 1)
		if self.state == 3 :
			self.state = 4
		interface.acquisition("Pour continuer, vous devez saisir délicatement la graine avec une pince à épiler que vous aurez \
			préalablement désinfectée et déposer la graine dans le pot dans lequel vous aurez fait un trou de 3 cm de profondeur \
			( un demi-doigt). La graine sera introduite avec le germe vers le bas, vous reboucherez ensuite sans trop tasser."
			,["ok"], [[self, "A5", [interface, None]]])


	def A6(self, interface, reponse=None):
		# Acquisition engrais
		if self.state == 5 :
			self.state = 6

		if reponse == None :
			interface.acquisition("Voulez-vous utiliser des engrais ? ",["Oui", "Non"], [[self, "A6", [interface, "oui"]], [self, "A6", [interface, "non"]]])

		if reponse == "oui" or reponse == "non" :
			self.Engrais = (reponse == 'oui')

		if self.Engrais:
			if reponse == 1 or reponse == 2 :
				self.Engrais_freq = int(reponse)
				self.A7(interface)

			else :
				interface.elmt_afficher = []
				interface.boutons = []
				interface.printTexte(20, "Quelle est la quantité à mettre dans un litre ? (en mL) ?\
				 Cette information devrait se situer derrière la bouteille.")
				rep = interface.input(200, 200)
				self.Engrais_quantite = int(rep)

				interface.acquisition("Quelle est la fréquence d'utilisation de l'engrais ? (1 pour à chaque arrosage, 2 pour \
					un arrosage pour deux.",["1", "2"], [[self, "A6", [interface, 1]], [self, "A6", [interface, 2]]])

		if self.Engrais == False :
			self.A7(interface)


	def acquisition_taille(self, interface, reponse =None, rep = None, reaffiche = False):
		# Acquisition taille

		interface.acquisition("Quelle est la taille de votre plante ? (en cm)", None, None)
		rep = interface.input(200, 200)

		self.Taille = int(rep)



	def A11(self, interface):
		if self.state == 10 :
			self.state = 11
		interface.acquisition("Félicitation, au cours de ces quelques mois vous avez certainement beaucoup appris sur le jardinage !"
			, ["ok"], [[interface, "accueil"]])

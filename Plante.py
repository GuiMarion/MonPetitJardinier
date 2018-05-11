
class Plante :

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

	def getName(self):
		return self.Name

	def q(self, state):

		self.state = state

		print("Voulez-vous quitter ? o/n")
		q = input()
		while q != 'o' and q != 'n':
			q = input("Nous n'avons pas compris.")

		return (q == 'o')


	def A1(self):
		# Acquisition pot/terre
		print("Bonjour, vous avez decidez de planter une plante avec notre logiciel, bravo ! \
			Nous avons tout d'abord besoin d'une information, voulez-vous planter en pot ou en terre ? (p/t)")

		rep = input()

		while rep != 'p' and rep != 't':
			rep = input("Nous n'avons pas compris \n")

		print("Très bien.")

		self.Pot = (rep == 'p')


		if self.q(1):
			return(self)
		self.A2()

	def A2(self):
		# Procédure germination

		if self.Pot:
			print("Vous avez choisi de panter en pot, c'est une très bonne idée. Pour cela \
				nous vous conseillons de mettre vos graines dans du coton humide pour les faire\
				germer. Revenez nous voir une fois fait.")
		else :
			print("Vous evez choisi de planter en terre, c'est une très bonne idée. Pour cela \
				nous vous conseillons de mettre vos graines directement dans la terre. Revenez nous voir \
				une fois une pousse sortie de la terre.")


		if self.q(2):
			return(self)
		self.A3()

	def A3(self):
		# Acquisition germination

		if self.Pot:

			print("Votre graine a-t-elle germée ? (o/n)")

			rep = input()

			while rep != 'o' and rep != 'n':
				rep = input("Nous n'avons pas compris\n")

			if rep == 'n':
				print("Revenez vers nous une fois qu'elle aura germée.")
				self.A3()
			else :

				if self.q(3):
					return(self)
				self.A4()

		else: 
			print("Avez-vous apperçu un germe sortir ?")
			# Intégrer photos
			rep = input()

			while rep != 'o' and rep != 'n':
				rep = input("Nous n'avons pas compris\n")

			if rep == 'n':
				print("Revenez vers nous une fois qu'elle aura germée.")
			else :

				if self.q(3):
					return(self)
				self.A5()		


	def A4(self):
		# Procédure pour mettre la graine en terre (cas Pot = 1)

		print("Pour continuer, vous devez saisir délicatement la graine avec une pince à épiler que vous aurez\
			préalablement désinfectée et la déposer dans le pot dans lequel vous aurez fait un trou de 3 cm de profondeur\
			( un demi-doigt). La graine sera introduite avec le germe vers le bas, vous reboucherez ensuite sans trop tasser.")
		
		if self.q(4):
			return(self)
		self.A5()	

	def A5(self):
		# Acquisition lumière

		print("Votre plante est desormais en terre, il lui faudra maintenant de la lumière pour vivre.\
			Vous pouvez utiliser une lampe agricole ou bien la lumière naturelle, cependant \
			il vous faudra beaucoup de lumière, la lumière naturelle sera donc appropriée dans une région\
			ensoleillée et qui n'est pas à l'ombre. Une lampe agricole peut être utilisée seule ou en\
			complément et devra être d'au moins 125-250 watts (ce qui a un coût en élécricité.)\n\
			Que voulez-vous faire ? (lampe/exte)  ")	


		rep = input()

		while rep != "lampe" and rep != "exte":
			rep = input("Nous n'avons pas compris\n")

		if rep == "lampe":
			self.Lampe = True
			print("C'est un très bon choix. La lampe est-elle une HPS ? (o/n)")

			rep = input()
			while rep != 'o' and rep != 'n':
				rep = input()

			self.Lampe_HPS = (rep == 'o')

			print("Quelle est la puissance (en watts)")

			rep = input()

			self.Lampe_puissance = rep

		else:
			print("C'est un très bon choix. Nous attirons votre attention sur le fait qu'il vous faut\
				être attentif à l'ensoleillement de votre plante (au moins 6h de plein soleil par jours)\
				ainsi qu'au risque climatique et naturels (grêle, pluit, vente, ...) que notre application\
				ne pourra pas prévoir.")



		if self.q(4):
			return(self)
		self.A6()


	def A6(self):
		print("prout")
		return(self)

	def launch(self):

		switcher = {
			1: self.A1,
			2: self.A2,
			3: self.A3,
			4: self.A4,
			5: self.A5,
			6: self.A6
		}


		switcher[self.state]()

		return (self)



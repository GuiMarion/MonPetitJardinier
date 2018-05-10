
class Plante :

	def __init__(self, name):

		# We declare all variables we need for printing
		self.Name = name
		self.state = 1
		self.Pot = None
		self.T = None 
		self.Lampe = None
		self.Lampe_model = None 
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

		if self.Pot:
			print("Vous avez choisi de panter en pot, c'est une très bonne idée. Pour cela \
				nous vous conseillons de mettre vos graines dans du coton humide pour les faire\
				germer. Revenez nous voir une fois fait.")
		else :
			print("Vous evez choisi de planter en terre, c'est une très bonne idée. Pour cela \
				nous vous conseillons de mettre vos graines directe dans la terre. Revenez nous voir \
				une fois une pousse sortie de la terre.")

		if self.q(2):
			return(self)

	def A3(self):
		print("A3")


	def launch(self):

		switcher = {
			1: self.A1,
			2: self.A2,
			3: self.A3
		}


		switcher[self.state]()

		return (self)



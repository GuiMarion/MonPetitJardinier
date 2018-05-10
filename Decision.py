
class Plante :

	def __init__(self, name):

		# We declare all variables we need for printing
		self.Name = name
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

	def getName():
		return self.Name

	def A1(self):
		print("Bonjour, vous avez decidez de planter une plante avec notre logiciel, bravo ! \
			Nous avons tout d'abord besoin d'une information, voulez-vous planter en pot ou en terre ? (p/t)")

		rep = input()

		while rep != 'p' and rep != 't':
			rep = input("Nous n'avons pas compris \n")

		print("Très bien.")

		self.Pot = (rep == 'p')

	def A2(self):

		if self.Pot:
			print("Vous avez choisi de panter en pot, c'est une très bonne idée. Pour cela \
				nous vous conseillons de mettre vos graines dans du coton humide pour les faire\
				germer. Revenez nous voir une fois fait.")
		else :
			print("Vous evez choisi de planter en terre, c'est une très bonne idée. Pour cela \
				nous vous conseillons de mettre vos graines directe dans la terre. Revenez nous voir \
				une fois une pousse sortie de la terre.")

	def launch(self):
		self.A1()
		self.A2()




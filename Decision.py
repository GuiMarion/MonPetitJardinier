
class Decisions :

	def __init__(self):

		# We declare all variables we need for printing
		Pot = None
		T = None 
		Lampe = None
		Lampe_model = None 
		Lampe_puissance = None
		Engrais = None
		Engrais_freq = None
		Engrais_quantite = None
		Taille = None
		Floraison = None

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

D = Decisions()

D.launch()




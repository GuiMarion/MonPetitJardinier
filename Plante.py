
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

	def q(self, state):

		self.state = state

		print("Voulez-vous quitter ? o/n")
		q = input()
		while q != 'o' and q != 'n':
			q = input("Nous n'avons pas compris.")

		return (q == 'o')

	def Recolte(self):

		if (self.Floraison_début - datetime.datetime.now()) > 25:
			print("La floraison arrive à grand pas, vous pouvez dès à présent recolter les fruits qui vous semblent\
				murs. Bravo, notre travail est terminé !")

			return(self)


	def Arrosage(self):

		if (self.Arrosage_last - datetime.datetime.now()).days > 3:
			print("Il est temps d'arroser, pour cela remplissez lentement le pot d'eau. Il faut qu'après\
			l'arrosage le pot soit beaucoup plus lourd qu'avant, 3 litres devraient suffirent.")

		if self.Engrais:
			print("Vous devraient aussi mettre de l'engrais, pour cela ajouter ", self.Engrais_quantite, "par litre d'eau.")

		self.Arrosage_last = datetime.datetime.now()

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

			self.Lampe_puissance = int(rep)

		else:
			print("C'est un très bon choix. Nous attirons votre attention sur le fait qu'il vous faut\
				être attentif à l'ensoleillement de votre plante (au moins 6h de plein soleil par jours)\
				ainsi qu'au risque climatique et naturels (grêle, pluit, vente, ...) que notre application\
				ne pourra pas prévoir.")



		if self.q(5):
			return(self)
		self.A6()

	def A6(self):
		# Acquisitino engrais

		print("Voulez-vous utiliser des engrais ? (o/n)")
		rep = input()
		while rep != 'o' and rep != 'n':
			rep = input()

		self.Engrais = (rep == 'o')

		if self.Engrais:
			print("Quelle est la quantité à mettre dans un litre ? (en mL) ? Cette information devrait se situer derriere \
				la bouteille.")

			rep = input()

			self.Engrais_quantite = int(rep)

		if self.q(6):
			return(self)
		self.A7()


	def A7(self):
		# Affichage croissance

		if self.Lampe:
			print("Vous allez devoir installer votre lampe agricole. Il faut la placer sur un porte lampe, que vous pouvez\
				construire vous même avec des cables/ficelle et une structure métalique, il faut que l'installation permette\
				de changer la hauteur de la lampe quand on le désire. Placer pour l'instant la lampe 10 cm au dessus de la plante.\
				La photopériode doit être reglée entre à 18h de lumière par jour, utiliser une minuteur que vous pourrez\
				vous procurer dans le commerce. Utiliser un reflecteur au dessus de la lampe afin de perdre le moins\
				de lumière possible est une bonne pratique.\n\
				Une fois fait, bravo ! Votre plante est desormais en phase de croissance, vous n'avez plus qu'à utiliser\
				l'application pour savoir quand arroser et mettre les engrais, nous vous demanderons régulièrement\
				la taille de vos plantes afin de vous indiquer les prochaines démarches.")

		else :
			print("Bravo ! Votre plante est desormais en phase de croissance, vous n'avez plus qu'à utiliser\
				l'application pour savoir quand arroser et mettre les engrais, nous vous demanderons régulièrement\
				la taille de vos plantes afin de vous indiquer les autres démarches à suivre.")

		if self.q(7):
			return(self)
		self.A8()

	def A8(self):

		# Acquisition taille
		print("Quelle est la taille de votre plante ? (en cm)")
		rep = input()
		self.Taille = int(rep)

		if self.q(8):
			return(self)
		self.A9()

	def A9(self):

		#Affichage rempotage/ taille/ floraison

		if self.Taille >15 and self.Pot and self.Rempoter == 0:
			print("Il est temps de rempoter votre plante. Pour cela attendez le prochain arrosage et avant d'arroser,\
				sortez votre plante de son pot en tapant sur l'arrière du pot. Vous devriez pouvoir sortir la motte de\
				terre sans l'abimer. Ensuite remplissez aux trois quarts le pot de taille supèrieure, creuser un trou\
				de la taille de la motte de terre que vous avez sortie, et glissez là à l'interieur. Soupoudrez le tout\
				de terreau, tassez, puis arrosez.")
			self.Rempoter +=1

		if self.Taille > 25 and self.Pot and self.Rempoter == 1:
			print("Il est temps de rempoter votre plante. Pour cela attendez le prochain arrosage et avant d'arroser,\
				sortez votre plante de son pot en tapant sur l'arrière du pot. Vous devriez pouvoir sortir la motte de\
				terre sans l'abimer. Ensuite remplissez aux trois quarts le pot de taille supèrieure, creuser un trou\
				de la taille de la motte de terre que vous avez sortie, et glissez là à l'interieur. Soupoudrez le tout\
				de terreau, tassez, puis arrosez.")
			self.Rempoter +=1

		if self.Taille > 30 and self.Lampe:
			print("Il est temps de passer à la période de floraison, pour cela il faut changer de lampe, pour\
				mettre une lampe spéciale floraison (elle a un spectre plus chaud, plus jaune). Et réduire la\
				photopériode à 12h de lumière par jour. ")

		if self.Taille > 35:
			print("Vous devriez voir apparaître les premières fleurs, si c'est le cas, il est temps d'effectuer\
			la taille de votre plante. Il vous faut couper les petits débuts de fleurs qui sont trop bas pour prendre\
			la lumière (les gourmandes) et les parties qui ne prendrons pas la lumière. Ne coupez pas les grosses feuilles,\
			elles contiennent beaucoup d'energie que la plante peut quand même utiliser, s'il elle n'en a plue besoin\
			elle s'en débarassera d'elle même.")

			if self.q(9):
				return(self)
			self.A10()

		else :	
			self.A8()

	def A10(self):
		# Acquisition floraison
		print("Vous devriez être passé en floraison et avoir effectué les premières tailles. Est-ce bien le cas ? (o/n")

		rep = input()
		while rep != 'o' and rep != 'n':
			rep = input("Nous n'avons pas compris\n")

		if rep == 'o':
			self.Floraison = True
			self.Floraison_début = datetime.date.today()
			print("Très bien vous pouvons continuer")
		else :
			print("Nous vous conseillons de revenir aux étapes précédentes afin d'effectuer ces procédures.")

		if self.q(10):
			return(self)
		self.A11()

	def A11(self):

		print("C'est fini")
		return self

	def launch(self):

		switcher = {
			1: self.A1,
			2: self.A2,
			3: self.A3,
			4: self.A4,
			5: self.A5,
			6: self.A6,
			7: self.A7,
			8: self.A8,
			9: self.A9,
			10: self.A10,
			11: self.A11
		}


		switcher[self.state]()

		return (self)



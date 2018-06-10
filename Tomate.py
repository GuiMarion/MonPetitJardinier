import datetime
import Plante


class Tomate(Plante.Plante):

	# TODO afficher arrosage et ajustement taille lampe

	def __init__(self, name):
		Plante.Plante.__init__(self,name)
		self.type = "tomate"
		self.state = 3
		self.etapes = [
			"A1",
			"A2",
			"A3",
			"A4",
			"A5",
			"A6",
			"A7",
			"A8",
			"A9",
			"A10",
			"A11"
		]


	def Recolte(self):

		if (self.Floraison_debut - datetime.datetime.now()) > 25:
			print("La floraison arrive à grand pas, vous pouvez dès à présent recolter les fruits qui vous semblent\
				murs. Bravo, notre travail est terminé !")

			return(self)

	def A5(self, interface, reponse=None):
		# Acquisition lumière
		if self.state == 4 :
			self.state = 5

		if reponse == None :
			interface.acquisition("Votre plante est desormais en terre, il lui faudra maintenant de la lumière pour vivre.\
				Vous pouvez utiliser une lampe agricole ou bien la lumière naturelle, cependant \
				il vous faudra beaucoup de lumière, la lumière naturelle sera donc appropriée dans une région\
				ensoleillée et qui n'est pas à l'ombre. Une lampe agricole peut être utilisée seule ou en\
				complément et devra être d'au moins 125-250 watts (ce qui a un coût en élécricité.)\n\
				Que voulez-vous faire ?",["lampe", "lumiere naturelle"], [[self, "A5", [interface, "lampe"]], [self, "A5", [interface, "lumiere naturelle"]]])


		if reponse == "lampe":
			self.Lampe = True
			interface.acquisition("C'est un très bon choix. La lampe est-elle une HPS ? "
			,["oui", "non"], [[self, "A5", [interface, "HPS"]], [self, "A5", [interface, "non HPS"]]])

		if reponse == "HPS" :
			self.Lampe_HPS = True

			print("Quelle est la puissance (en watts)")
			rep = interface.input(200, 200)
			self.Lampe_puissance = int(rep)
			self.A6(interface, None)

		elif reponse == "lumiere naturelle":
			self.Lampe = False
			interface.acquisition("C'est un très bon choix. Nous attirons votre attention sur le fait qu'il vous faut\
				être attentif à l'ensoleillement de votre plante (au moins 6h de plein soleil par jours)\
				ainsi qu'au risque climatique et naturels (grêle, pluit, vent, ...) que notre application\
				ne pourra pas prévoir.",["ok"], [[self, "A6", [interface, None]]])



	def A7(self, interface):
		# Affichage croissance
		if self.state == 6 :
			self.state = 7

		if self.Lampe:
				interface.acquisition("Vous allez devoir installer votre lampe agricole. Il faut la placer sur un porte lampe, que vous pouvez\
					construire vous même avec des cables/ficelle et une structure métalique, il faut que l'installation permette\
					de changer la hauteur de la lampe quand on le désire. Placer pour l'instant la lampe 10 cm au dessus de la plante.\
					La photopériode doit être reglée à 18h de lumière par jour, utiliser un minuteur que vous pourrez\
					vous procurer dans le commerce. Utiliser un reflecteur au dessus de la lampe afin de perdre le moins\
					de lumière possible est une bonne pratique.", ["ok"], [[interface, "accueil"]])


	def A8(self, interface):
		# Affichage croissance
		if self.state == 7 :
			self.state = 8

		if self.Lampe:

				interface.acquisition("Bravo ! Votre plante est desormais en phase de croissance, vous n'avez plus qu'à utiliser\
					l'application pour savoir quand arroser et mettre les engrais, nous vous demanderons régulièrement\
					la taille de vos plantes afin de vous indiquer les prochaines démarches."
					,["ok"], [[interface, "accueil"]])

		else :
				interface.acquisition("Bravo ! Votre plante est desormais en phase de croissance, vous n'avez plus qu'à utiliser\
					l'application pour savoir quand arroser et mettre les engrais, nous vous demanderons régulièrement\
					la taille de vos plantes afin de vous indiquer les autres démarches à suivre."
					, ["ok"], [[interface, "accueil"]])




	def A9(self, interface):
		#Affichage rempotage/ taille/ floraison
		if self.state == 8 :
			self.state = 9

		if (self.Taille >15 and self.Pot and self.Rempoter == 0) or (self.Taille > 25 and self.Pot and self.Rempoter == 1):
			interface.acquisition("Il est temps de rempoter votre plante. Pour cela attendez le prochain arrosage et avant d'arroser,\
				sortez votre plante de son pot en tapant sur l'arrière du pot. Vous devriez pouvoir sortir la motte de\
				terre sans l'abimer. Ensuite remplissez aux trois quarts le pot de taille supèrieure, creuser un trou\
				de la taille de la motte de terre que vous avez sortie, et glissez là à l'interieur. Soupoudrez le tout\
				de terreau, tassez, puis arrosez."
				, ["d'accord"], [[interface, "accueil"]])

			self.Rempoter +=1

		if self.Taille > 30 and self.Lampe:
			interface.acquisition("Il est temps de passer à la période de floraison, pour cela il faut changer de lampe, pour\
				mettre une lampe spéciale floraison (elle a un spectre plus chaud, plus jaune). Et réduire la\
				photopériode à 12h de lumière par jour."
				, ["d'accord"], [[interface, "accueil"]])

		if self.Taille > 35:
			interface.acquisition("Vous devriez voir apparaître les premières fleurs, si c'est le cas, il est temps d'effectuer\
			la taille de votre plante. Il vous faut couper les petits débuts de fleurs qui sont trop bas pour prendre\
			la lumière (les gourmandes) et les parties qui ne prendrons pas la lumière. Ne coupez pas les grosses feuilles,\
			elles contiennent beaucoup d'energie que la plante peut quand même utiliser, s'il elle n'en a plue besoin\
			elle s'en débarassera d'elle même."
				, ["d'accord"], [[self, "A10", [interface, None]]])

			self.A10()

		else :
			interface.acquisition("Vous n'avez rien a faire pour le moment."
				, ["d'accord"], [[interface, "accueil"]])


	def A10(self, interface, reponse=None):
		# Acquisition floraison
		if self.state == 9 :
			self.state = 10

		if reponse == None :
			interface.acquisition("Vous devriez être passé en floraison et avoir effectué les premières tailles. Est-ce bien le cas ?"
				, ["oui", "non"], [[self, "A10", [interface, "oui"]], [self, "A10", [interface, "non"]]])

		if reponse == 'oui' :
			self.Floraison = True
			self.Floraison_début = datetime.date.today()
			interface.acquisition("Très bien vous pouvons continuer"
				, ["ok"], [[self, "A11", interface]])
		else :
			interface.acquisition("Nous vous conseillons de revenir aux étapes précédentes afin d'effectuer ces procédures."
				, ["ok"], [[interface, "ma_plante", self]])

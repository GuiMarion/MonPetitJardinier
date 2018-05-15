import pickle
from Plante import *
import sys
from Interface import *

class App:
	def __init__(self):
		self.Plantes = pickle.load(open(".state", 'rb'))
		names = []
		for elem  in self.Plantes:
			names.append(elem.getName())
		self.gui = Gui(names)

	def quit(self):

		self.gui.pop_up("au revoir", "Merci d'avoir utilisé l'application, à bientôt.")
		pickle.dump(self.Plantes, open(".state", 'wb'), pickle.HIGHEST_PROTOCOL)

	def reset(self):

		self.gui.pop_up("", "Vos plantes sont effacées.")
		pickle.dump([], open(".state", 'wb'), pickle.HIGHEST_PROTOCOL)

	def Start(self):
		print("Bienvenu dans l'application : Mon Petit Jardinier.")

		if len(self.Plantes) == 0:
			print("Vous n'avez pas de plantes en cours, nous en crééons une, comment dois-je l'appeler ?")
			name = input()
			self.Plantes.append(Plante(name))
			self.Plantes[-1] = self.Plantes[-1].launch()

		else:
			print("Voulez-vous créer une plante ? (o/n)")
			choix = input()

			while choix != 'o' and choix != 'n':
				choix = input("Nous n'avons pas compris")


			if choix == 'o':
				print("Comment dois-je l'appeler ?")
				name = input()
				self.Plantes.append(Plante(name))
				self.Plantes[-1] = self.Plantes[-1].launch()

			elif len(self.Plantes) > 1:
				print("Vous avez plusieurs plantes en cours, laquelle voulez vous lancer ?")

				for i in range(len(self.Plantes)) :
					print(self.Plantes[i].getName(), ":",i)

				choix = int(input())
				while choix < 0 or choix >= len(self.Plantes):
					print(choix)
					choix = input("Nous n'avons pas compris ...\n")

				self.Plantes[choix] = self.Plantes[choix].launch()

			elif len(self.Plantes) == 1:

				print("Vous n'avez qu'une plante en cours, nous la lançons.")

				self.Plantes[0] = self.Plantes[0].launch()

			else:
				raise ValueError("Impossible choice")

		A.quit()


if __name__ == "__main__":

	A = App()

	if len(sys.argv) == 2:
		if sys.argv[1] == "reset":
			A.reset()
		elif sys.argv[1] == "Start":
			A.Start()
		else :
			print("Usage: Python3 RSA2.py <Message to encrypt>")


	else:
		print("Usage: Python3 App.py <Start or reset>")

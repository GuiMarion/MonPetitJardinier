# -*- coding: utf-8 -*-
import sys
from sdl2 import *
import sdl2.ext
import sdl2.sdlttf as sdlttf
from sdl2.sdlimage import *
import ctypes
from Tomate import *
from Basilic import *
import pickle


class Gui() :

	type_de_plantes = ["Tomate", "Basilic"] #type de plante : "tomate, "basilique", ...
	boutons = [] #[x,y,h,w, methode à appeler, argument(s)]
	definitions = []
	window = None
	run = True
	windowSurface = None
	police = None
	plantes = []
	historique = []
	elmt_afficher = []
	img_ok = SDL_LoadBMP(b"pictures/OK.bmp")



	def __init__(self, plantes):
		#initialisation de la sdl
		if SDL_Init(SDL_INIT_VIDEO) < 0  :
			print("problème d'initialisation : " + str(SDL_GetError()))

		#creation de la fenetre
		self.window = SDL_CreateWindow(b"mon petit jardinier",
								  SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
								  600, 600, SDL_WINDOW_SHOWN)
		if self.window == None :
			print("erreur lors de la creation de la fenetre.")

		self.windowSurface = SDL_GetWindowSurface(self.window)
		#initialisation de sdl_ttf
		sdlttf.TTF_Init()

		self.plantes = plantes

	def start(self):

		self.accueil()

		while self.run :
			for plante in self.plantes :
				plante.Arrosage(self)
			self.affichage()


	def printT(self, size, x, y, text, font = "SanFranciscoRegular", color = [0,0,0]):

		pas = size
		L = []
		k = 0
		while k < len(text):
			if text[k] == '\n':
				L.append(text[:k])
				text = text[(k+1):]
				k = 0
				if L[-1][0] == " ":
					L[-1] = L[-1][1:]

			else :
				k += 1

		L.append(text)
		try :
			if L[-1][0] == " ":
				L[-1] = L[-1][1:]
		except :
			pass

		police =  sdlttf.TTF_OpenFont(str.encode("Fonts/"+font+".ttf"), size)

		P = 0

		for elem in L:
			Text = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(elem), SDL_Color(color[0], color[1], color[2]))
			a = [Text, SDL_Rect(x,y + P)]
			self.elmt_afficher.append(a)
			P += pas

		sdlttf.TTF_CloseFont(police)

	def printD(self, size, x, y, text, font = "SanFranciscoRegular", color = [0,0,0]):

		pas = size
		L = []
		k = 0
		MOD = 20


		i = len(text)-1
		while i > 0:
			if text[i] == '\t' or text[i] == '\n':
				text = text[:i] + text[i+1:]
			i = i -1


		M = ""
		for i in range(len(text)):
			M += text[i]
			if i % MOD == 0 and i != 0:
				M += '-\n'

		text = M
		while k < len(text):
			if text[k] == '\n':
				L.append(text[:k])
				text = text[(k+1):]
				k = 0
				if L[-1][0] == " ":
					L[-1] = L[-1][1:]

			else :
				k += 1

		L.append(text)

		for i in range(len(L)):
			if L[i] == '':
				del L[i]

		police =  sdlttf.TTF_OpenFont(str.encode("Fonts/"+font+".ttf"), size)

		P = 0

		print(L)

		for elem in L:
			Text = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(elem), SDL_Color(color[0], color[1], color[2]))
			a = [Text, SDL_Rect(x,y + P)]
			self.elmt_afficher.append(a)
			P += pas

		sdlttf.TTF_CloseFont(police)



	def printTexte(self, size, text, font = "SanFranciscoRegular", color = [0, 0, 0]):

		definition = []
		mots_definie = []
		pas = size
		L = []
		k = 0
		MOD = 45

		Deb = 100
		Deby = 120

		i = len(text)-1
		while i > 0:
			if text[i] == '\t' or text[i] == '\n':
				text = text[:i] + text[i+1:]
			i = i -1

		if "<def" in text :
			a = text.find("<def")
			b = text.find(">")
			definition.append(text[(a+6):].split(text[b:])[0])	#on recupere la definition et le mot associé
			c = text.find("</def>")
			mots_definie.append(text[(b+1):].split(text[c:])[0])

			text = text[:a] + text[(b+1):]		#on supprime les balises du texte
			c = text.find("</def>")
			text = text[:c] + text[(c+6):]

		M = ""
		for i in range(len(text)):
			M += text[i]
			if i % MOD == 0 and i != 0:
				M += '-\n'

		text = M
		while k < len(text):
			if text[k] == '\n':
				L.append(text[:k])
				text = text[(k+1):]
				k = 0
				if L[-1][0] == " ":
					L[-1] = L[-1][1:]

			else :
				k += 1

		L.append(text)

		for i in range(len(L)):
			if L[i] == '':
				del L[i]

		print(L)
		if L[-1][0] == " ":
			L[-1] = L[-1][1:]

		police =  sdlttf.TTF_OpenFont(str.encode("Fonts/"+font+".ttf"), size)

		P = 0

		print(L)

		for elem in L:
			afficher = False
			for i in range(len(mots_definie)) :
				if mots_definie[i] in elem :
					mots = mots_definie[i]
					afficher = True
					print(mots)
					position = elem.find(mots)
					fin_mots = len(mots) + position
					Text = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(elem[:position]), SDL_Color(0, 0, 0))
					a = [Text, SDL_Rect(Deb,Deby + P)]
					self.elmt_afficher.append(a)

					Text = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(elem[position:].split(elem[fin_mots:])[0]), SDL_Color(50, 50, 150))
					pos = Deb + int(position*8.5)
					a = [Text, SDL_Rect(pos,Deby + P)]
					self.elmt_afficher.append(a)
					self.definitions.append([definition[i], pos, Deby+P+2, Deb+fin_mots*9+2, P+pas+Deby])

					Text = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(elem[fin_mots:]), SDL_Color(color[0], color[1], color[2]))
					a = [Text, SDL_Rect(Deb + fin_mots*9+2,Deby + P)]
					self.elmt_afficher.append(a)

					P += pas

			if not afficher :
				print(elem)
				Text = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(elem), SDL_Color(color[0], color[1], color[2]))
				a = [Text, SDL_Rect(Deb,Deby + P)]
				self.elmt_afficher.append(a)
				P += pas

		sdlttf.TTF_CloseFont(police)


	#nettoie l'ecran entre deux appel à une fenetre.
	def clean(self) :
		#colorie la fenetre en blanc
		SDL_FillRect(self.windowSurface, None, 0xffffff)



	def bouton_retour_arriere(self) :
		if(len(self.historique) >= 2) :
			if [(0, 0, 25, 24), self, "retour_arriere"] not in self.boutons :
				img = SDL_LoadBMP(str.encode("pictures/retour.bmp"))
				self.elmt_afficher.append([img, SDL_Rect(0, 0)])
				self.boutons.append([(0, 0, 25, 24), self, "retour_arriere"])


	def retour_arriere(self) :
		try :
			fenetre = self.historique[-2]
			f = getattr(fenetre[0], fenetre[1])
			del self.historique[-1] #on supprime de l'historique la fenetre que l'on quitte.

			if len(fenetre) < 3 :
				f()
			else :
				if(len(fenetre) >= 3) :
					if(type(fenetre[2]) is list) :
						f(*fenetre[2])
					else :
						f(fenetre[2])
		except :
			#print("historique indisponible")
			pass


	#verifie les clics
	def event(self) :
		#boucle de gestion des evenements (cliques de la souris)
		event = SDL_Event()
		while SDL_PollEvent(ctypes.byref(event)) != 0:
			if event.type == SDL_QUIT:
				self.run = False
				break
			#si on clique sur un bouton on appel la fonction associé
			if event.type == SDL_MOUSEBUTTONUP:
				for button in self.boutons :
					if (event.button.x >= button[0][0] and event.button.x <= button[0][2] and event.button.y >= button[0][1] and event.button.y <= button[0][3]) :
						f = getattr(button[1], button[2])

						if(len(button) > 3) :
							if(type(button[3]) is list) :
								f(*button[3])
							else :
								f(button[3])
						else :
							f()



	#affiche la fenetre en cours et verifie les events.
	def affichage(self) :
		#nettoyage de la fenetre actuelle.
		self.clean()
		self.bouton_retour_arriere()

		#affichage de la fenetre courante.
		for a in self.elmt_afficher :
			SDL_BlitSurface(a[0], None, self.windowSurface, a[1])

		#on affiche les definitions si necessaire :
		x, y = ctypes.c_int(0), ctypes.c_int(0)
		buttonstate = sdl2.mouse.SDL_GetMouseState(ctypes.byref(x), ctypes.byref(y))
		temp = len(self.elmt_afficher)
		for definition in self.definitions :
			if (definition[1] <= x.value and definition[3] >= x.value and definition[2] <= y.value and definition[4] >= y.value) :
				self.printD(20, x.value+10, y.value+10, definition[0], color = [51, 57, 255])
				for i in range(len(self.elmt_afficher) - temp) :
					SDL_BlitSurface(self.elmt_afficher[temp+i][0], None, self.windowSurface, self.elmt_afficher[temp+i][1])
				del self.elmt_afficher[-temp:]

		#verification des events.
		self.event()

		#mis a jour de l'affichage de la fenetre (rien n'est afficher avant)
		SDL_UpdateWindowSurface(self.window)

		SDL_Delay(15)


	#fenetre d'ajout de plante.
	def nouvelle_plante(self) :

		deb = 120
		pas = 240
		H = 250

		self.boutons = []
		self.elmt_afficher = []
		self.definitions = []
		if self.historique[-1] != [self, "nouvelle_plante"] :
			self.historique.append([self, "nouvelle_plante"])

		self.printT(50, 90, 15, "Mon petit jardinier")

		for i in range(len(self.type_de_plantes)) :
			img = SDL_LoadBMP(str.encode("pictures/" + self.type_de_plantes[i] + ".bmp"))
			self.elmt_afficher.append([img, SDL_Rect(i*pas + deb, H)])
			#création du bouton
			self.boutons.append([(i*pas + deb , H, i*pas + deb +100 , H +130), self, "creation_plante", self.type_de_plantes[i]])


	#fonction ajoutant une plante à self.plante
	def creation_plante(self, type_de_plantes) :
		#ask name
		self.elmt_afficher = []
		self.boutons = []
		self.definitions = []

		self.printT(20, 50, 100, "quelle nom souhaitez vous donnez à votre plante ?")
		name = self.input(200, 200)

		p = eval(type_de_plantes)(name)
		self.plantes.append(p)
		self.plantes[-1].A1(self, None)


	#fenetre d'affichage de plante.
	def ma_plante(self, plante) :
		self.elmt_afficher = []
		self.boutons = []
		self.definitions = []
		self.historique.append([self,  "ma_plante", [plante]])

		self.printT(60, 250, 10, plante.getName())

		past_task = plante.etapes[:plante.state]
		advised_task =plante.etapes[plante.state]
		futur_task = plante.etapes[(plante.state+1):]

		for i in range(len(past_task)) :
			self.printT(20, i*60+10, 120, str(past_task[i]))
			self.boutons.append([(i*60+10, 120, i*60+35, 145), plante, past_task[i], self])

		"""for i in range(len(advised_task)) :
			if advised_task[i][0] == "a temps" :
				color = SDL_Color(150, 233, 150)
			elif advised_task[i][0] == "trop tôt" :
				color = SDL_Color(255, 255, 102)
			else :
				color = SDL_Color(230, 230, 255)
		"""
		#color = SDL_Color(230, 230, 255)
		self.printT(40, 250, 220, str(advised_task))
		self.boutons.append([(245, 220, 300, 270), plante, advised_task, self])

		for i in range(len(futur_task)) :
			self.printT(20, i*80+10, 420, str(futur_task[i]))
			self.boutons.append([(i*80+10, 420, i*80+42, 445), plante, futur_task[i], self])


	#affiche la fenetre d'accueil.
	def accueil(self) :

		deb = 30
		pas = 120
		H = 400

		self.historique.append([self, "accueil"])
		self.boutons = []
		self.elmt_afficher = []
		self.definitions = []
		#load the pictures of the plants.
		img_tomate = SDL_LoadBMP(b"pictures/Tomate.bmp")
		img_basilic = SDL_LoadBMP(b"pictures/Basilic.bmp")

		self.printT(50, 90, 15, "Mon petit jardinier")

		for i in range(len(self.plantes)) :
			if (type(self.plantes[i]) == Tomate) :
				self.elmt_afficher.append([img_tomate, SDL_Rect(i*pas + deb, H)])
			else :
				self.elmt_afficher.append([img_basilic, SDL_Rect(i*pas + deb, H)])

			self.boutons.append([(i*pas + deb , H, i*pas + deb +100 , H +130), self, "ma_plante", self.plantes[i]])
			#self.printT(60, i*70, 400, self.plantes[i].getName())

		self.printT(30, 400, H, "nouvelle \n plante")
		self.boutons.append([(400, H, 510, H + 100), self, "nouvelle_plante"])


	#fenetre d'acquisition. reponse sous la forme [reponse1, reponse2...]. action sous la forme [[]]
	def acquisition(self, question, reponses, action) :

		Deb = 120
		pas = 240
		H = 250

		self.boutons = []
		self.elmt_afficher = []
		self.definitions = []
		if self.historique[-1] != [self, "acquisition", [question, reponses, action]] :
			self.historique.append([self, "acquisition", [question, reponses, action]])

		self.printTexte(20,question)

		H += (len(question)**2)//2000

		try :
			if len(reponses) == 1:

				if reponses[0] == "ok":
					self.elmt_afficher.append([self.img_ok, SDL_Rect(pas + Deb - 130, H + 30)])

				else:
					self.printT(30, pas + Deb - 130, H + 30, reponses[0])

				if len(action[0]) == 3 :
					self.boutons.append([(pas + Deb - 130, H, pas + Deb - 30, H +100), action[0].pop(0), action[0].pop(0), action[0].pop(0)])
				else :
					self.boutons.append([(pas + Deb - 130, H, pas + Deb - 30, H+100), action[0].pop(0), action[0].pop(0)])


			if len(reponses) == 2:

				for i in range(len(reponses)) :
					self.printT(20, i*pas + Deb, H, reponses[i])

					if len(action[i]) == 3 :
						self.boutons.append([(i*pas + Deb, H, i*pas + Deb + 100, H +100), action[i].pop(0), action[i].pop(0), action[i].pop(0)])
					else :
						self.boutons.append([(i*pas + Deb, H, i*pas + Deb +100, H+100), action[i].pop(0), action[i].pop(0)])
		except :
			pass


	#affiche une pop-up (géré directement par gnome/kde/..., pas par la sdl)
	def pop_up(self, title, text) :
		SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_INFORMATION, str.encode(title), str.encode(text), self.window)


	def input(self, x, y) :
		text = ""
		finie = False
		event = SDL_Event()

		while(not finie) :
			while ( SDL_PollEvent( event ) ) :
				if ( event.type == SDL_KEYDOWN ) :
					if event.key.keysym.sym == SDLK_ESCAPE :
						finie = True
					elif event.key.keysym.sym == SDLK_KP_ENTER :
						finie = True
					elif event.key.keysym.sym ==  SDLK_RETURN:
						finie = True
					elif event.key.keysym.sym == SDLK_BACKSPACE :
						temp = list(text)
						del temp[-1]
						text = "".join(temp)

					else :
						try :
							text = text + chr(event.key.keysym.sym)
						except :
							pass

			self.printT(25, x, y, text+"|")
			self.affichage()
			del self.elmt_afficher[-1]
			SDL_Delay(15)

		return text

	def quit(self):

		self.pop_up("au revoir", "Merci d'avoir utilisé l'application, à bientôt.")
		pickle.dump(self.plantes, open(".state", 'wb'), pickle.HIGHEST_PROTOCOL)

	def reset(self):

		self.pop_up("", "Vos plantes sont effacées.")
		pickle.dump([], open(".state", 'wb'), pickle.HIGHEST_PROTOCOL)


def Load():
	Plantes = pickle.load(open(".state", 'rb'))
	return Plantes

if __name__ == "__main__":


	if len(sys.argv) == 2:
		App = Gui(Load())
		if sys.argv[1] == "Reset":
			App.reset()
		elif sys.argv[1] == "Start":

			App.start()
			App.quit()
			#il faut sauvegarder le nouvel état des plantes
		else :
			print("Usage: Python3 App.py <Start or Reset>")


	else:
		print("Usage: Python3 App.py <Start or Reset>")

# -*- coding: utf-8 -*-
import sys
from sdl2 import *
import sdl2.ext
import sdl2.sdlttf as sdlttf
from sdl2.sdlimage import *
import ctypes
from Tomate import *
from Basilic import *


class Gui() :

	type_de_plantes = ["Tomate", "Basilic"] #type de plante : "tomate, "basilique", ...
	boutons = [] #[x,y,h,w, methode à appeler, argument(s)]
	window = None
	run = True
	windowSurface = None
	police = None
	plantes = []
	historique = []
	elmt_afficher = []


	def __init__(self, plantes):
		#initialisation de la sdl
		if SDL_Init(SDL_INIT_VIDEO) < 0  :
			print("probléme d'initialisation : " + str(SDL_GetError()))

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

	def printT(self, size, x, y, text, font = "SanFranciscoRegular"):

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
		if L[-1][0] == " ":
			L[-1] = L[-1][1:]

		police =  sdlttf.TTF_OpenFont(str.encode("Fonts/"+font+".ttf"), size)

		P = 0

		for elem in L:
			Text = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(elem), SDL_Color(0, 0, 0))
			a = [Text, SDL_Rect(x,y + P)]
			self.elmt_afficher.append(a)
			P += pas

		sdlttf.TTF_CloseFont(police)

	def printTexte(self, size, text, font = "SanFranciscoRegular"):

		pas = size
		L = []
		k = 0
		MOD = 45 # ?

		Deb = 100
		Deby = 120

		M = ""
		for i in range(len(text)):
			M += text[i]
			if i % MOD == 0 and i != 0:
				M += '\n'

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

		for elem in L:
			Text = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(elem), SDL_Color(0, 0, 0))
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
			#load the pictures of the plants.
			img = IMG_LoadTexture(self.renderer, str.encode("pictures/retour.jpg"))
			SDL_RenderCopy(self.renderer, img, None, self.creation_rectangle("sdl_rect", 0, 0, 5, 5))
			SDL_DestroyTexture(img)
			self.boutons.append([self.creation_rectangle("bouton", 0, 0, 5, 5), self, "retour_arriere"])


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
						print("islist")
						print(fenetre[2])
						f(*fenetre[2])
					else :
						f(fenetre[2])
		except :
			print("historique indisponible")


	#verifie les clics
	def event(self) :
		#boucle de gestion des evenements (cliques de la souris)
		event = SDL_Event()
		while SDL_PollEvent(ctypes.byref(event)) != 0:
			if event.type == SDL_QUIT:
				a.run = False
				break
			#si on clique sur un bouton on appel la fonction associé
			if event.type == SDL_MOUSEBUTTONUP:
				for button in self.boutons :
					if (event.button.x >= button[0][0] and event.button.x <= button[0][2] and event.button.y >= button[0][1] and event.button.y <= button[0][3]) :
						print("button[1]")
						if (len(button) <= 3) :
							self.historique.append([button[1], button[2]])
						f = getattr(button[1], button[2])

						if(len(button) > 3) :
							if(type(button[3]) is list) :
								f(*button[3])
								#self.historique.append([button[1], button[2], button[3]])
							else :
								f(button[3])
								self.historique.append([button[1], button[2], button[3]])
						else :
							f()



	#affiche la fenetre en cours et verifie les events.
	def affichage(self) :
		#nettoyage de la fenetre actuelle.
		self.clean()
		#self.bouton_retour_arriere()

		#affichage de la fenetre courante.
		for a in self.elmt_afficher :
			SDL_BlitSurface(a[0], None, self.windowSurface, a[1])

		#pour permettre de visualiser les boutons :
		for button in self.boutons :
			SDL_FillRect(self.windowSurface, SDL_Rect(button[0][0], button[0][1], (button[0][2] - button[0][0]), (button[0][3] -button[0][1])), 0x200002)
			print(button[0])

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
		#name = input()
		name = "toto"
		p = eval(type_de_plantes)(name)
		self.plantes.append(p)
		self.plantes[-1].A1(self, None)

	#fenetre d'affichage de plante.
	def ma_plante(self, plante) :
		self.elmt_afficher = []
		self.boutons = []
		self.historique.append([self,  "ma_plante", [plante]])

		self.printT(60, 10, 10, plante.getName())

		past_task = plante.etapes[:plante.state]
		advised_task =plante.etapes[plante.state]
		futur_task = plante.etapes[(plante.state+1):]

		for i in range(len(past_task)) :
			self.printT(60, i*60+10, 120, str(past_task[i]))

		"""for i in range(len(advised_task)) :
			if advised_task[i][0] == "a temps" :
				color = SDL_Color(150, 233, 150)
			elif advised_task[i][0] == "trop tôt" :
				color = SDL_Color(255, 255, 102)
			else :
				color = SDL_Color(230, 230, 255)
		"""
		#color = SDL_Color(230, 230, 255)
		self.printT(60, 80, 220, str(advised_task))
		self.boutons.append([(80, 220, 90, 230), plante, advised_task, self])

		for i in range(len(futur_task)) :
			self.printT(60, i*80+10, 420, str(futur_task[i]))


	#affiche la fenetre d'accueil.
	def accueil(self) :

		deb = 30
		pas = 120
		H = 400

		self.historique.append([self, "accueil"])
		self.boutons = []
		self.elmt_afficher = []
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
		self.historique.append([self, "acquisition", [question, reponses, action]])

		"""nbr_ligne = len(question)//100 + 1
		for num_ligne in range(nbr_ligne) :
			texte = sdlttf.TTF_RenderUTF8_Blended(self.police, str.encode(question[100*num_ligne:100*(num_ligne+1)]), SDL_Color(0, 0, 0))
			texture = SDL_CreateTextureFromSurface(self.renderer, texte)
			self.elmt_afficher.append([self.renderer, texture, None, self.creation_rectangle("sdl_rect", 0, 10*num_ligne, 1*len(question[100*num_ligne:100*(num_ligne+1)]), 10)])
			SDL_FreeSurface(texte)
		"""
		self.printTexte(20,question)

		H += (len(question)**2)//2000

		if len(reponses) == 1:

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


	#affiche une pop-up (géré directement par gnome/kde/..., pas par la sdl)
	def pop_up(self, title, text) :
		SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_INFORMATION, str.encode(title), str.encode(text), self.window)


#exemple d'utilisation :

plante_existante = [Basilic("toto")]
plante_existante.append(Tomate("titi"))
a = Gui(plante_existante)

#a.nouvelle_plante()
a.accueil()

#boucle principale du programme doit être de cette forme (ce qui doit être ajouté doit-être avant le event())
while a.run :
	a.affichage()

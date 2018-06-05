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
    police = "Fonts/angelina.ttf"

    #fonction temporaire :
    def pprint(self,a) :
        print(a)

    def __init__(self, plantes):
        #initialisation de la sdl
        if SDL_Init(SDL_INIT_VIDEO) < 0  :
            print("probléme d'initialisation : " + str(SDL_GetError()))

        #creation de la fenetre
        self.window = SDL_CreateWindow(b"mon petit jardinier",
                                  SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                                  592, 460, SDL_WINDOW_SHOWN | SDL_WINDOW_RESIZABLE)
        if self.window == None :
            print("erreur lors de la creation de la fenetre.")

        self.windowSurface = SDL_GetWindowSurface(self.window)
        #initialisation de sdl_ttf
        sdlttf.TTF_Init()

        self.plantes = plantes

    def printT(self, size, x, y, font, text):
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


        for elem in L:
            Text = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(elem), SDL_Color(0, 0, 0))
            a = [Text, None, self.windowSurface, SDL_Rect(x,y)]
            self.elmt_afficher.append(a)

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



    #x,y,largeur et hauteur sont des pourcentage de la taille de la fenetre. type = "sdl_rect" ou "bouton"
    def creation_rectangle(self, type, x,y,largeur, hauteur) :
        #récupére la taille de l'ecran.
        largeur_ecran = ctypes.pointer(ctypes.c_int(0))
        hauteur_ecran = ctypes.pointer(ctypes.c_int(0))
        SDL_GetWindowSize(self.window, largeur_ecran, hauteur_ecran)
        largeur_ecran = largeur_ecran.contents.value
        hauteur_ecran = hauteur_ecran.contents.value

        #calcul du rectangle
        x = x * largeur_ecran // 100
        largeur = largeur * largeur_ecran // 100
        y = y * hauteur_ecran // 100
        hauteur = hauteur * hauteur_ecran // 100
        if type == "sdl_rect" :
            return SDL_Rect(x, y, largeur, hauteur)
        else :
            return x, y, largeur+x, hauteur+y

    #affiche la fenetre en cours et verifie les events.
    def affichage(self) :
        #nettoyage de la fenetre actuelle.
        self.clean()
        self.bouton_retour_arriere()

        #affichage de la fenetre courante.
        for a in self.elmt_afficher :
            SDL_BlitSurface(a[0], a[1], a[2], a[3])

        #verification des events.
        self.event()
        #mis a jour de l'affichage de la fenetre (rien n'est afficher avant)
        SDL_UpdateWindowSurface(self.window)

        SDL_Delay(15)


    #fenetre d'ajout de plante.
    def nouvelle_plante(self) :
        self.boutons = []
        self.elmt_afficher = []
        self.historique.append([self, "nouvelle_plante"])

        couleurNoire = SDL_Color(0, 0, 0)#couleur du texte
        texte = sdlttf.TTF_RenderUTF8_Blended(self.police, b"Mon petit jardinier", couleurNoire)  #creation du texte
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)    #creation d'une texture depuis le texte
        SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", 10, 5, 80, 5));  #applique la texture sur la fenetre dans un rectangle

        for i in range(len(self.type_de_plantes)) :
            img = IMG_LoadTexture(self.renderer, str.encode("pictures/" + self.type_de_plantes[i] + ".png"))
            self.elmt_afficher.append([self.renderer, img, None, self.creation_rectangle("sdl_rect", (i+1)*12, 33, 10, 10)])
            #création du bouton
            self.boutons.append([self.creation_rectangle("bouton", (i+1)*12, 33, 10, 10), self, "creation_plante", self.type_de_plantes[i]])


    #fonction ajoutant une plante à self.plante
    def creation_plante(self, type_de_plantes) :
        print(self.historique)
        print("\n\n\n")
        del(self.historique[-1])
        #ask name
        #name = input()
        name = "toto"
        p = eval(type_de_plantes)(name)
        self.plantes.append(p)
        self.plantes[-1].A1(self, None)

    #fenetre d'affichage de plante.
    def ma_plante(self, plante) :
        self.elmt_afficher = []
        self.bouton = []
        self.historique.append([self,  "ma_plante", [plante]])

        texte = sdlttf.TTF_RenderUTF8_Blended(self.police, str.encode(plante.getName()), SDL_Color(0, 0, 0))  #création du texte
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)                #creation d'une texture depuis le texte
        self.elmt_afficher.append([self.renderer, texture, None, self.creation_rectangle("sdl_rect", 34, 5, 8, 6)])
        SDL_FreeSurface(texte)
        past_task = plante.etapes[:plante.state]
        advised_task =plante.etapes[plante.state]
        futur_task = plante.etapes[(plante.state+1):]

        for i in range(len(past_task)) :
            SDL_RenderFillRect(self.renderer, self.creation_rectangle("sdl_rect", i*12, 22, 11, 10))
            texte = sdlttf.TTF_RenderUTF8_Blended(self.police, str.encode(str(past_task[i])), SDL_Color(0, 0, 0))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            self.elmt_afficher.append([self.renderer, texture, None, self.creation_rectangle("sdl_rect", i*12, 22, 11, 10)])
            SDL_FreeSurface(texte)

        """for i in range(len(advised_task)) :
            if advised_task[i][0] == "a temps" :
                color = SDL_Color(150, 233, 150)
            elif advised_task[i][0] == "trop tôt" :
                color = SDL_Color(255, 255, 102)
            else :
                color = SDL_Color(230, 230, 255)
        """
        color = SDL_Color(230, 230, 255)
        SDL_RenderFillRect(self.renderer, self.creation_rectangle("sdl_rect", i*20+4, 44, 22, 20))
        texte = sdlttf.TTF_RenderUTF8_Blended(self.police, str.encode(advised_task), color)
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)
        self.elmt_afficher.append([self.renderer, texture, None, self.creation_rectangle("sdl_rect", i*20+4, 44, 22, 20)])
        self.boutons.append([self.creation_rectangle("bouton", i*20+4, 44, 22, 20), plante, advised_task, self])
        SDL_FreeSurface(texte)

        for i in range(len(futur_task)) :
            sdl_rect = self.creation_rectangle("sdl_rect", i*10+4, 20*(i//10)+86, 11, 10)
            SDL_RenderFillRect(self.renderer, sdl_rect)
            texte = sdlttf.TTF_RenderUTF8_Blended(self.police, str.encode(str(futur_task[i])), SDL_Color(0, 0, 0))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            self.elmt_afficher.append([self.renderer, texture, None, sdl_rect])
            SDL_FreeSurface(texte)


    #affiche la fenetre d'accueil.
    def accueil(self) :
        self.historique.append([self, "accueil"])
        self.boutons = []
        self.elmt_afficher = []
        #load the pictures of the plants.
        img_tomate = SDL_LoadBMP(b"pictures/Tomate.bmp")
        img_basilic = SDL_LoadBMP(b"pictures/Basilic.bmp")

        police =  sdlttf.TTF_OpenFont(str.encode(self.police), 20)
        couleurNoire = SDL_Color(0, 0, 0)
        #texte = sdlttf.TTF_RenderUTF8_Blended(police, b"Mon petit jardinier", couleurNoire); #création du texte

        #a = [texte, None, self.windowSurface, SDL_Rect(10,10)]
        #self.elmt_afficher.append(a)

        self.printT(60, 10, 10, "angelina", "Mon petit jardinier")

        for i in range(len(self.plantes)) :
            if (type(self.plantes[i]) == Tomate) :
                self.elmt_afficher.append([img_tomate, None, self.windowSurface, SDL_Rect(i*50, 300)])
            else :
                self.elmt_afficher.append([img_basilic, None, self.windowSurface, SDL_Rect(i*50, 300)])
            self.boutons.append([self.creation_rectangle("bouton", (i+1)*12, 75, 10, 10), self, "ma_plante", self.plantes[i]])

            texte = sdlttf.TTF_RenderUTF8_Blended(police, str.encode(self.plantes[i].getName()), couleurNoire); #création du texte
            self.elmt_afficher.append([texte, None, self.windowSurface, SDL_Rect(i*50, 400)])

        SDL_FillRect(self.windowSurface, SDL_Rect(80, 75, 90, 90), 0x200002)

        #SDL_SetRenderDrawColor(self.renderer, 200, 200, 200, 255)   #colorie un retangle (pour materialiser le bouton)
        #SDL_RenderFillRect(self.renderer, self.creation_rectangle("sdl_rect", 80, 75, 10, 10))
        #texte = sdlttf.TTF_RenderUTF8_Blended(self.police, str.encode("nouvelle plante"), SDL_Color(0, 0, 0))  #on met du texte sur le bouton
        texte = sdlttf.TTF_RenderUTF8_Blended(police, b"nouvelle plante", couleurNoire); #création du texte
        self.elmt_afficher.append([texte, None, self.windowSurface, SDL_Rect(100, 100)])
        self.boutons.append([self.creation_rectangle("bouton", 80, 75, 10, 10), self, "nouvelle_plante"])


    #fenetre d'acquisition. reponse sous la forme [reponse1, reponse2...]. action sous la forme [[]]
    def acquisition(self, question, reponse, action) :
        self.boutons = []
        self.elmt_afficher = []
        self.historique.append([self, "acquisition", [question, reponse, action]])

        nbr_ligne = len(question)//100 + 1
        for num_ligne in range(nbr_ligne) :
            texte = sdlttf.TTF_RenderUTF8_Blended(self.police, str.encode(question[100*num_ligne:100*(num_ligne+1)]), SDL_Color(0, 0, 0))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            self.elmt_afficher.append([self.renderer, texture, None, self.creation_rectangle("sdl_rect", 0, 10*num_ligne, 1*len(question[100*num_ligne:100*(num_ligne+1)]), 10)])
            SDL_FreeSurface(texte)

        for i in range(len(reponse)) :
            sdl_rect = self.creation_rectangle("sdl_rect", 17+i*12, 10*nbr_ligne+10, 10, 10)
            SDL_SetRenderDrawColor(self.renderer, *self.creation_rectangle("bouton", 17+i*12, 10*nbr_ligne+10, 10, 10))   #colorie un retangle (pour materialiser le bouton)
            SDL_RenderFillRect(self.renderer, sdl_rect)
            texte = sdlttf.TTF_RenderUTF8_Blended(self.police, str.encode(str(reponse[i])), SDL_Color(0, 0, 0))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            self.elmt_afficher.append([self.renderer, texture, None, sdl_rect])
            if len(action[i]) == 3 :
                self.boutons.append([self.creation_rectangle("bouton", 17+i*12, 10*nbr_ligne+10, 10, 10), action[i].pop(0), action[i].pop(0), action[i].pop(0)])
            else :
                self.boutons.append([self.creation_rectangle("bouton", 17+i*12, 10*nbr_ligne+10, 10, 10), action[i].pop(0), action[i].pop(0)])
            SDL_FreeSurface(texte)


    #affiche une pop-up (géré directement par gnome/kde/..., pas par la sdl)
    def pop_up(self, title, text) :
        SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_INFORMATION, str.encode(title), str.encode(text), self.window)

    #affiche un diagnostique (a modifier quand les actions sont pretes)
    def diagnostique(self, text) :
        couleurNoire = SDL_Color(0, 0, 0)
        texte = sdlttf.TTF_RenderUTF8_Blended(self.police, str.encode(text), couleurNoire)    #creation eds textes
        texte2 = sdlttf.TTF_RenderUTF8_Blended(self.police, b"ok", couleurNoire)
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)            #creation des textures
        texture2 = SDL_CreateTextureFromSurface(self.renderer, texte2)

        self.elmt_afficher([self.renderer, texture, None, self.creation_rectangle("sdl_rect", 5, 5, 60, 90)])
        #créer le bouton qui renvoie à l'ecran d'accueil
        self.elmt_afficher.append([self.renderer, texture2, None, self.creation_rectangle("sdl_rect", 67, 76, 8, 12)])
        self.boutons.append([self.creation_rectangle("bouton", 67, 76, 8, 12), self, "accueil"])    #creation du bouton



#exemple d'utilisation :

plante_existante = [Basilic("toto")]
plante_existante.append(Tomate("titi"))
a = Gui(plante_existante)

#a.nouvelle_plante()
a.accueil()

#boucle principale du programme doit être de cette forme (ce qui doit être ajouté doit-être avant le event())
while a.run :
    a.affichage()

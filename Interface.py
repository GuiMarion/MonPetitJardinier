import sys
from sdl2 import *
import sdl2.sdlttf as sdlttf
from sdl2.sdlimage import *
import ctypes
from Tomate import *
from Basilic import *

class Gui() :

    plantes = [] #type de plante : "tomate, "basilique", ...
    boutons = [] #[x,y,h,w, methode à appeler, argument(s)]
    window = None
    run = True
    windowSurface = None
    renderer = None
    police = None
    plantes = []
    historique = None

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
        #creation d'un renderer
        self.renderer = SDL_CreateRenderer(self.window, -1, 0)
        if self.renderer == None :
            print("erreur lors de la creation du renderer.")

        self.police =  sdlttf.TTF_OpenFont(b"Roboto.ttf", 65)
        self.plantes = plantes
        self.historique = [[self, "accueil"]]

    #nettoie l'ecran entre deux appel à une fenetre.
    def clean(self) :
        #suppression des boutons.
        self.boutons = []
        #colorie la fenetre en blanc
        SDL_SetRenderDrawColor(self.renderer, 255, 255, 255, 255)
        #nettoie la fenetre
        SDL_RenderClear(self.renderer)


    def bouton_retour_arriere(self) :
        if(len(self.historique) >= 2) :
            #load the pictures of the plants.
            img = IMG_LoadTexture(self.renderer, str.encode("pictures/retour.jpg"))
            SDL_RenderCopy(self.renderer, img, None, self.creation_rectangle("sdl_rect", 0, 0, 5, 5))
            self.boutons.append([self.creation_rectangle("bouton", 0, 0, 5, 5), self, "retour_arriere"] )


    def retour_arriere(self) :
        #on supprime tout de suite retour_arriere de l'historique
        del self.historique[-1]

        fenetre = self.historique[-2]
        f = getattr(fenetre[0], fenetre[1])
        del self.historique[-1] #on supprime de l'historique la fenetre que l'on quitte.
        if len(fenetre) < 3 :
            f()
        else :
            f(fenetre[2])

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
                        if (len(button) <= 3) :
                            self.historique.append([button[1], button[2]])
                        f = getattr(button[1], button[2])

                        if(len(button) > 3) :
                            f(button[3])
                            self.historique.append([button[1], button[2], button[3]])
                        else :
                            f()

        SDL_Delay(15)


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
        #recuperation de la fenetre courante.
        self.historique.append(["temp data"])
        self.historique.append(["temp data"])
        self.retour_arriere()
        #verification des events.
        self.event()
        #mis a jour de l'affichage de la fenetre (rien n'est afficher avant)
        SDL_RenderPresent(self.renderer)


    #fenetre d'ajout de plante.
    def nouvelle_plante(self) :
        #load the pictures of the plants.
        img_tomate = IMG_LoadTexture(self.renderer, str.encode("pictures/icone_tomate.png"))
        img_basilic = IMG_LoadTexture(self.renderer, str.encode("pictures/basilic.png"))

        couleurNoire = SDL_Color(0, 0, 0)#couleur du texte
        texte = sdlttf.TTF_RenderText_Solid(self.police, b"Mon petit jardinier", couleurNoire)  #creation du texte
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)    #creation d'une texture depuis le texte
        SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", 10, 5, 80, 5));  #applique la texture sur la fenetre dans un rectangle

        for i in range(len(self.plantes)) :
            if (self.plantes[i].type == "tomate") :
                SDL_RenderCopy(self.renderer, img_tomate, None, self.creation_rectangle("sdl_rect", (i+1)*12, 33, 10, 10))
            else :
                SDL_RenderCopy(self.renderer, img_basilic, None, self.creation_rectangle("sdl_rect", (i+1)*12, 33, 10, 10))

            #création du bouton
            self.boutons.append([self.creation_rectangle("bouton", (i+1)*12, 33, 10, 10), self, "pprint", " il faut lier ce bouton à fonction_pour_creer_une_plante(type_de_plante)"])


    #fenetre d'affichage de plante.
    def ma_plante(self, name, past_task, advised_task, futur_task) :
        texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(name), SDL_Color(0, 0, 0))  #création du texte
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)                #creation d'une texture depuis le texte
        SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", 34, 5, 8, 6))    #applique la texture sur la fenetre dans un rectangle

        for i in range(len(past_task)) :
            SDL_RenderFillRect(self.renderer, self.creation_rectangle("sdl_rect", i*10+2, 22, 11, 10))
            texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(str(past_task[i])), SDL_Color(0, 0, 0))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", i*10+2, 22, 11, 10))

        for i in range(len(advised_task)) :
            if advised_task[i][0] == "a temps" :
                color = SDL_Color(150, 233, 150)
            elif advised_task[i][0] == "trop tôt" :
                color = SDL_Color(255, 255, 102)
            else :
                color = SDL_Color(230, 230, 255)

            SDL_RenderFillRect(self.renderer, self.creation_rectangle("sdl_rect", i*20+4, 44, 22, 20))
            texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(str(advised_task[i][1])), color)
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", i*20+4, 44, 22, 20))

        for i in range(len(futur_task)) :
            sdl_rect = self.creation_rectangle("sdl_rect", i*10+4, 20*(i//10)+86, 11, 10)
            SDL_RenderFillRect(self.renderer, sdl_rect)
            texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(str(futur_task[i])), SDL_Color(0, 0, 0))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            SDL_RenderCopy(self.renderer, texture, None, sdl_rect)


    #affiche la fenetre d'accueil.
    def accueil(self) :
        #load the pictures of the plants.
        img_tomate = IMG_LoadTexture(self.renderer, str.encode("pictures/icone_tomate.png"))
        img_basilic = IMG_LoadTexture(self.renderer, str.encode("pictures/basilic.png"))

        couleurNoire = SDL_Color(0, 0, 0)
        texte = sdlttf.TTF_RenderText_Solid(self.police, b"Mon petit jardinier", couleurNoire); #création du texte
        texture = SDL_CreateTextureFromSurface(self.renderer, texte);               #creation d'une texture depuis le texte
        SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", 10, 5, 80, 5));  #applique la texture sur la fenetre dans un rectangle

        for i in range(len(self.plantes)) :
            if (type(self.plantes[i]) == Tomate) :
                SDL_RenderCopy(self.renderer, img_tomate, None, self.creation_rectangle("sdl_rect", (i+1)*12, 75, 10, 10))
            else :
                SDL_RenderCopy(self.renderer, img_basilic, None, self.creation_rectangle("sdl_rect", (i+1)*12, 75, 10, 10))
            self.boutons.append([self.creation_rectangle("bouton", (i+1)*12, 75, 10, 10), self, "pprint", str("appel a la fonction qui appele la fonction ma_plante pour la plante " + self.plantes[i].getName())] )

            texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(self.plantes[i].getName()), SDL_Color(0, 0, 0))  #on met du texte sur le bouton
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", (i+1)*12, 82, 10, 10))

        SDL_SetRenderDrawColor(self.renderer, 200, 200, 200, 255)   #colorie un retangle (pour materialiser le bouton)
        SDL_RenderFillRect(self.renderer, self.creation_rectangle("sdl_rect", 80, 75, 10, 10))
        texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode("nouvelle plante"), SDL_Color(0, 0, 0))  #on met du texte sur le bouton
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)
        SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", 80, 75, 10, 10))
        self.boutons.append([self.creation_rectangle("bouton", 80, 75, 10, 10), self, "nouvelle_plante"])


    #fenetre d'acquisition. question sous la forme [question, reponse1, reponse2, reponse3, ..., fonction à appeller]
    def acquisition(self, question) :
        texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(str(question[0])), SDL_Color(0, 0, 0))
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)
        SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", 17, 11, 8, 51))

        for i in range(1, len(question)-1) :
            sdl_rect = self.creation_rectangle("sdl_rect", 17, 33+((i-1)*22), 34, 22)
            SDL_SetRenderDrawColor(self.renderer, 200, 200, 200, 255)   #colorie un retangle (pour materialiser le bouton)
            SDL_RenderFillRect(self.renderer, sdl_rect)
            texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(str(question[i])), SDL_Color(0, 0, 0))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            SDL_RenderCopy(self.renderer, texture, None, sdl_rect)
            self.boutons.append([self.creation_rectangle("bouton", 17, 33+((i-1)*22), 34, 22), question[-2], str(question[-1]), str(question[i])])


    #pop-up
    def pop_up(self, title, text) :
        SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_INFORMATION, str.encode(title), str.encode(text), self.window) #affiche une pop-up (géré directement par gnome/kde/..., pas par la sdl)

    #affiche un diagnostique (a modifier quand les actions sont pretes)
    def diagnostique(self, text) :
        couleurNoire = SDL_Color(0, 0, 0)
        texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(text), couleurNoire)    #creation eds textes
        texte2 = sdlttf.TTF_RenderText_Solid(self.police, b"ok", couleurNoire)
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)            #creation des textures
        texture2 = SDL_CreateTextureFromSurface(self.renderer, texte2)
        SDL_RenderCopy(self.renderer, texture, None, self.creation_rectangle("sdl_rect", 5, 5, 60, 90))   #applique les textures sur la fenetre
        #créer le bouton qui renvoie à l'ecran d'accueil
        SDL_RenderCopy(self.renderer, texture2, None, self.creation_rectangle("sdl_rect", 67, 76, 8, 12))
        self.boutons.append([self.creation_rectangle("bouton", 67, 76, 8, 12), self, "accueil"])    #creation du bouton



#exemple d'utilisation :

plante_existante = [Basilic("toto")]
plante_existante.append(Tomate("titi"))
a = Gui(plante_existante)

#a.nouvelle_plante()
a.accueil()
#a.acquisition(["ma question blablabla","oui","non","je ne sais pas",a,"pprint"])
#a.diagnostique("ta plante a un probleme")
#a.ma_plante("toto", [1,2,5], [["a temps","arrosage"],["trop tard","rempotage"],["trop tôt","mettre de l'engrais"]], [4,8,3])

#boucle principale du programme doit être de cette forme (ce qui doit être ajouté doit-être avant le event())
while a.run :
    a.affichage()

import sys
from sdl2 import *
import sdl2.sdlttf as sdlttf
import ctypes


class Gui() :

    plantes = [] #type de plante : "tomate, "basilique", ...
    boutons = [] #[x,y,h,w, action]
    window = None
    run = True
    windowSurface = None
    police = None
    type_plante= ["tomate", "basilic"]

    def __init__(self):
        SDL_Init(SDL_INIT_VIDEO)
        window = SDL_CreateWindow(b"mon petit jardinier",
                                  SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                                  592, 460, SDL_WINDOW_SHOWN)
        windowSurface = SDL_GetWindowSurface(window)
        sdlttf.TTF_Init();
        self.renderer = SDL_CreateRenderer(window, -1, 0)

    #nettoie l'ecran entre deux appel à une fenetre.
    def clean(self) :
        SDL_SetRenderDrawColor(self.renderer, 255, 255, 255, 255)
        SDL_RenderClear(self.renderer)


    #verifie les clics
    def affichage(self) :
        SDL_UpdateWindowSurface(self.window)
        event = SDL_Event()
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                a.run = False
                break
        #ajouter un if pour detecter les clique sur self.boutons[]
        SDL_Delay(15)


    #fenetre d'ajout de plante.
    def nouvelle_plante(self) :
        self.clean()

        police = sdlttf.TTF_OpenFont(b"Roboto.ttf", 65)
        couleurNoire = SDL_Color(0, 0, 0)
        texte = sdlttf.TTF_RenderText_Solid(police, b"Mon petit jardinier", couleurNoire);
        texture = SDL_CreateTextureFromSurface(self.renderer, texte);
        SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(100, 20, 250, 150));

        for i in range(len(self.type_plante)) :
            SDL_SetRenderDrawColor(self.renderer, 10, 10, 10, 255)
            SDL_RenderFillRect(self.renderer, SDL_Rect((i+1)*75, 150, 50, 50))
            self.boutons.append([(i+1)*75, 200, (i+1)*75+50, 400, "fonction_pour_creer_une_plante(type_de_plante)"])

        SDL_RenderPresent(self.renderer)


    #fenetre d'affichage de plante.
    def ma_plante(self, plante) :
        pass

    #affiche la fenetre d'accueil.
    def accueil(self, plantes) :
        self.clean()

        police = sdlttf.TTF_OpenFont(b"Roboto.ttf", 65)
        couleurNoire = SDL_Color(0, 0, 0)
        texte = sdlttf.TTF_RenderText_Solid(police, b"Mon petit jardinier", couleurNoire);
        texture = SDL_CreateTextureFromSurface(self.renderer, texte);
        SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(100, 50, 200, 150));

        for i in range(len(plantes)) :
            SDL_SetRenderDrawColor(self.renderer, 10, 10, 10, 255)
            SDL_RenderFillRect(self.renderer, SDL_Rect((i+1)*75, 350, 50, 50))
            self.boutons.append([(i+1)*75, 350, (i+1)*75+50, 400, "self.ma_plante(plantes[i])"])

        SDL_SetRenderDrawColor(self.renderer, 200, 200, 200, 255)
        SDL_RenderFillRect(self.renderer, SDL_Rect(400, 350, 50, 50))
        self.boutons.append([400, 350, 450, 400, "self.nouvelle_plante()"])

        SDL_RenderPresent(self.renderer)

    #fenetre d'acquisition.
    def acquisition(self) :
        pass

    #pop-up
    def pop_up(self, texte) :
        pass

    #affiche un diagnostique
    def diagnostique(self, text) :
        print(text)
        """
        police = sdlttf.TTF_OpenFont(b"Roboto.ttf", 65)
        couleurNoire = SDL_Color(0, 0, 0)
        texte = sdlttf.TTF_RenderText_Solid(police, text, couleurNoire);
        texture = SDL_CreateTextureFromSurface(self.renderer, texte);
        SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(100, 50, 200, 150));
        """




a = Gui()

a.nouvelle_plante()
a.accueil(["tomate"])
#boucle principale du programme doit être de cette forme (ce qui doit être ajouté doit-être avant le affichage())
while a.run :
    a.affichage()

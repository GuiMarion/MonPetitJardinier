import sys
from sdl2 import *
import sdl2.sdlttf as sdlttf
import ctypes


class Gui() :

    plantes = [] #type de plante : "tomate, "basilique", ...
    boutons = [] #[x,y,h,w, methode à appeler, argument(s)]
    window = None
    run = True
    windowSurface = None
    police = None
    type_plante = ["tomate", "basilic"]
    plantes = []

    #fonction temporaire :
    def pprint(self,a) :
        print(a)

    def __init__(self, plantes):
        SDL_Init(SDL_INIT_VIDEO)
        self.window = SDL_CreateWindow(b"mon petit jardinier",
                                  SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED,
                                  592, 460, SDL_WINDOW_SHOWN)
        self.windowSurface = SDL_GetWindowSurface(self.window)
        sdlttf.TTF_Init();
        self.renderer = SDL_CreateRenderer(self.window, -1, 0)
        self.police =  sdlttf.TTF_OpenFont(b"Roboto.ttf", 65)
        self.plantes = plantes

    #nettoie l'ecran entre deux appel à une fenetre.
    def clean(self) :
        self.boutons = []
        SDL_SetRenderDrawColor(self.renderer, 255, 255, 255, 255)
        SDL_RenderClear(self.renderer)


    #verifie les clics
    def affichage(self) :
        #SDL_UpdateWindowSurface(self.window)
        event = SDL_Event()
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if event.type == SDL_QUIT:
                a.run = False
                break
            #ajouter un if pour detecter les clique sur self.boutons[]
            if event.type == SDL_MOUSEBUTTONUP:
                for button in self.boutons :
                    if (event.button.x >= button[0] and event.button.x <= button[2] and event.button.y >= button[1] and event.button.y <= button[3]):
                        f = getattr(self, button[4])
                        print(button)
                        if(len(button) > 5) :
                            f(button[5])
                        else :
                            f()
        SDL_Delay(15)


    #fenetre d'ajout de plante.
    def nouvelle_plante(self) :
        self.clean()
        SDL_SetRenderDrawColor(self.renderer, 150, 150, 150, 255)

        couleurNoire = SDL_Color(0, 0, 0)
        texte = sdlttf.TTF_RenderText_Solid(self.police, b"Mon petit jardinier", couleurNoire)
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)
        SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(100, 20, 250, 150))

        for i in range(len(self.type_plante)) :
            SDL_SetRenderDrawColor(self.renderer, 10, 10, 10, 255)
            SDL_RenderFillRect(self.renderer, SDL_Rect((i+1)*75, 150, 50, 50))

            texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(str(self.type_plante[i])), SDL_Color(120, 120, 120))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            SDL_RenderCopy(self.renderer, texture, None, SDL_Rect((i+1)*75, 150, 50, 50))

            self.boutons.append([(i+1)*75, 150, (i+1)*75+50, 200, "pprint", " il faut lier ce bouton à fonction_pour_creer_une_plante(type_de_plante)"])

        SDL_RenderPresent(self.renderer)


    #fenetre d'affichage de plante.
    def ma_plante(self, name, past_task, advised_task, futur_task) :
        self.clean()
        SDL_SetRenderDrawColor(self.renderer, 150, 150, 150, 255)

        texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(name), SDL_Color(0, 0, 0))
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)
        SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(200, 20, 250, 50))

        for i in range(len(past_task)) :
            SDL_RenderFillRect(self.renderer, SDL_Rect(i*50+10, 100, 50, 50))
            texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(str(past_task[i])), SDL_Color(0, 0, 0))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(50*i+10, 100, 50, 50))

        for i in range(len(advised_task)) :
            if advised_task[i][0] == "a temps" :
                color = SDL_Color(150, 233, 150)
            elif advised_task[i][0] == "trop tôt" :
                color = SDL_Color(255, 255, 102)
            else :
                color = SDL_Color(230, 230, 255)
            SDL_RenderFillRect(self.renderer, SDL_Rect(i*100+20, 200, 100, 100))
            texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(str(advised_task[i][1])), color)
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(100*i+20, 200, 100, 100))

        for i in range(len(futur_task)) :
            SDL_RenderFillRect(self.renderer, SDL_Rect((i%10)*50+20, 100*(i//10)+400, 50, 50))
            texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(str(futur_task[i])), SDL_Color(0, 0, 0))
            texture = SDL_CreateTextureFromSurface(self.renderer, texte)
            SDL_RenderCopy(self.renderer, texture, None, SDL_Rect((i%10)*50+20, 100*(i//10)+400, 50, 50))

        SDL_RenderPresent(self.renderer)

    #affiche la fenetre d'accueil.
    def accueil(self) :
        self.clean()

        couleurNoire = SDL_Color(0, 0, 0)
        texte = sdlttf.TTF_RenderText_Solid(self.police, b"Mon petit jardinier", couleurNoire);
        texture = SDL_CreateTextureFromSurface(self.renderer, texte);
        SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(100, 50, 200, 150));

        for i in range(len(self.plantes)) :
            SDL_SetRenderDrawColor(self.renderer, 10, 10, 10, 255)
            SDL_RenderFillRect(self.renderer, SDL_Rect((i+1)*75, 350, 50, 50))
            self.boutons.append([(i+1)*75, 350, (i+1)*75+50, 400, "pprint", str("appel a la fonction qui appele la fonction ma_plante pour la plante " + self.plantes[i])] )

        SDL_SetRenderDrawColor(self.renderer, 200, 200, 200, 255)
        SDL_RenderFillRect(self.renderer, SDL_Rect(400, 350, 50, 50))
        self.boutons.append([400, 350, 450, 400, "nouvelle_plante"])

        SDL_RenderPresent(self.renderer)

    #fenetre d'acquisition.
    """    def acquisition(self, questions) :
        self.clean()
        i = 0
        j = 0
        for question in questions :
            for part in question :
                SDL_SetRenderDrawColor(self.renderer, 10, 10, 10, 255)
                SDL_RenderFillRect(self.renderer, SDL_Rect((j+1)*100+(i)*50, 350, 50, 50))
                self.boutons.append([(i+1)*75, 350, (j+1)*75+50, 400, "ma_plante", str(self.plantes[i])])
                i = i+1
            j = j +1
    """

    #pop-up
    def pop_up(self, title, text) :
        SDL_ShowSimpleMessageBox(SDL_MESSAGEBOX_INFORMATION,
                                     str.encode(title),
                                     str.encode(text),
                                     self.window)

    #affiche un diagnostique (a modifier quand les actions sont pretes)
    def diagnostique(self, text) :
        self.clean()
        couleurNoire = SDL_Color(0, 0, 0)
        texte = sdlttf.TTF_RenderText_Solid(self.police, str.encode(text), couleurNoire)
        texte2 = sdlttf.TTF_RenderText_Solid(self.police, b"ok", couleurNoire)
        texture = SDL_CreateTextureFromSurface(self.renderer, texte)
        texture2 = SDL_CreateTextureFromSurface(self.renderer, texte2)
        SDL_RenderCopy(self.renderer, texture, None, SDL_Rect(100, 50, 200, 150))
        #créer le bouton qui renvoie à l'ecran d'accueil
        SDL_RenderCopy(self.renderer, texture2, None, SDL_Rect(400, 350, 50, 50));
        self.boutons.append([400, 350, 450, 400, "accueil"])

        SDL_RenderPresent(self.renderer)


"""
#exemple d'utilisation :
plante_existante = ["ma tomate 1", "ma tomate 2"]
a = Gui(plante_existante)

a.nouvelle_plante()
a.accueil()
a.diagnostique("ta plante a un probleme")
#a.ma_plante("toto", [1,2,5], [["a temps","arrosage"],["trop tard","rempotage"],["trop tôt","mettre de l'engrais"]], [4,8,3])

#boucle principale du programme doit être de cette forme (ce qui doit être ajouté doit-être avant le affichage())
while a.run :
    a.affichage()
"""

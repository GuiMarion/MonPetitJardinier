# MonPetitJardinier
Mon Petit Jardiner est un projet de logiciel éducatif portant sur le jardinage.

Ce projet a été fait dans le cadre d'un cours à l'Université de Lyon dirigé par Stpéhanie Jean-Daubias. La code a été produit et appartient par Guilhem Marion et Luca Jourdan sous licence MIT.


# To get started

Le projet utilise python3 et SDL2, pour utiliser le logiciel installez les paquets suivants (sur une distribution de type Ubuntu) : 

		apt-get install python

		apt-get install libsdl2-dev

		apt-get install sdl2_ttf

		apt-get install sdl2_image

		pip install pysdl2

Pour archLinux : 

		pacman -S python

		pacman -S sdl2

		pacman -S sdl2_ttf

		pacman -S sdl2_image

		pip install pysdl2

Pour macOs : 

		brew install python

		brew install sdl2

		brew install sdl2_ttf

		brew install sdl2_image

		pip install pysdl2



# Usage 

		Usage: python3 App.py <Start or Reset>

Mon Petit Jardinier utilise une sauvegarde de toutes les plantes sur lesquelles vous travaillez, de ce fait c'est une mauvaise idée de quitter le programme en tuer le processus (cela ne sauvegardera pas votre avancement), utilisez donc la petite croix sur la fenêtre pour fermer le programme. 

Si vous voulez remettre à zéro vos plantes, utilisez le paramètre 'Reset': 

		python3 App.py Reset

Pour démarrer le programme : 

		python3 App.py Start

Vous êtes mainetenant prêt pour jardinner avec Mon Petit Jardinier ! 





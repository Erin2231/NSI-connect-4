#Les importations
import pygame
from pygame import mixer
pygame.init()
from pygame.locals import *
from random import randint
import math
clock =pygame.time.Clock()
mixer.init()

#Musique
mixer.music.load('sondefon.WAV')
mixer.music.set_volume(100)
mixer.music.play()
musiqueallumer=1

#Background
fond= pygame.image.load('minimal.JPG')
demarrage= pygame.image.load('demarragev2.PNG')
winner=pygame.image.load('the winner.JPG')
tiegame=pygame.image.load('tiegame.PNG')

#Fenêtre pygame
taille=largeur, hauteur = 950, 800
fenetre = pygame.display.set_mode(taille)
WHITE=(255,255,255)
BLACK=(0,0,0)

windowSurface=pygame.display.set_mode((largeur,hauteur),0,32)
fenetre.fill(WHITE)
fenetre.blit(demarrage,(300,300))

#Démarrage de pygame
running=True
turn=0

running = True
game_loop = True

turn=0

police = pygame.font.SysFont('Arial', 18, bold=True)
texte_2 = police.render ("Press 'm' to mute", True, (WHITE))

#Général loop
while running:
    clock.tick(60)
    #En cas d'un événement de pygame
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False
        #Si cliq sur l'écran, le "main loop commence"
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button==1:
            taille=largeur,hauteur=950,800
            fenetre = pygame.display.set_mode(taille)
            windowSurface=pygame.display.set_mode((largeur,hauteur),0,32)
            fenetre.fill((0, 0, 0))
            fenetre.blit(fond, (0, 0))
            grille=[[0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0],
                    [0,0,0,0,0,0]]
            running=True

            #Couleurs
            BLACK=(0,0,0)
            WHITE=(255,255,255)
            RED=(255,0,0)
            GREEN=(65,163,23)
            BLUE=(0,0,255)
            TURC=(37,253,233)
            aleatoir=(145,83,230)
            Grey=(60,60,60)
            YELLOW=(250,253,15)
            couleurs=[(GREEN),(WHITE)]

            #Interface grafique de la fenêtre pygame
            pygame.draw.rect(windowSurface,Grey,(700,440,145,145))
            pygame.draw.ellipse(windowSurface,WHITE,(707,530,130,40))
            pygame.draw.circle(windowSurface,GREEN,(773,480),35,0)
            turn=0
            police = pygame.font.SysFont('Arial', 18, bold=True)
            texte_3 = police.render ("Tour du joueur :", True, (Grey))
            fenetre.blit (texte_3, (720 ,538))
            pygame.display.flip()
            continuer = True


            #Grille principale graphique (jetons)
            a=50
            b=150
            for j in range(6):
                a=210
                for i in range(6):
                    pygame.draw.circle(windowSurface,Grey,(a,b),40,0)
                    a=a+80
                b=b+80
            turn = 0
            
            #Écrire sur l'écran le texte_2 ('m' to mute) 
            fenetre.blit (texte_2, (710 ,370))

            #JEUX SANS GRAPHIQUE
            #LA GRILLE DU DEBUT
            GRILLE = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
            lignes = 6
            colonnes=6

            #ACTIONS (les noms des fontions ce sont, à peut près, les actions qu'elles réalisent)
            def faire_tomber_une_piece (GRILLE, ligne, colonne, piece):
                GRILLE[ligne][colonne]=piece

            def ligne_valide(GRILLE, colonne):
                if colonne>=6  :
                    print("dehors")
                    return False
                else:
                    print(colonne, lignes-1)
                    return GRILLE[lignes-1][colonne]==0

            #Enregistrer la position de la souris
            position_souris = pygame.mouse.get_pos()

            def allez_a_la_ligne_valide(GRILLE, colonne):
                for i in range(lignes):
                    if GRILLE[i][colonne]==0:
                        return i

            def egalite():
                 if tie == 36 :
                    return True
                 else:
                    return False

            def affiche():
                for i in range(lignes):
                    print(GRILLE[i])

            #Cela sert a renverser la grille car pour la partie graphique la grille commence depuis le bas
            def GRILLE_inverse(GRILLE):
                idx = len(GRILLE) - 1
                GRILLE_inverse= []
                while (idx >= 0):
                    GRILLE_inverse.append(GRILLE[idx])
                    idx = idx - 1
                for i in range(lignes):
                    print(GRILLE_inverse[i])

            #Vérification des jetons pour gagner
            def verification_du_mouvement(GRILLE, piece):
                #Horizontale
                for c in range(colonnes-3):
                    for r in range(lignes):
                        if GRILLE[r][c] == piece and GRILLE[r][c+1] == piece and GRILLE[r][c+2] == piece and GRILLE[r][c+3] == piece:
                            return True
                #Verticale
                for c in range(colonnes):
                    for r in range(lignes-3):
                        if GRILLE[r][c] == piece and GRILLE[r+1][c] == piece and GRILLE[r+2][c] == piece and GRILLE[r+3][c] == piece:
                            return True
                #Diagonale vers en haut
                for c in range(colonnes-3):
                    for r in range(lignes-3):
                        if GRILLE[r][c] == piece and GRILLE[r+1][c+1] == piece and GRILLE[r+2][c+2] == piece and GRILLE[r+3][c+3] == piece:
                            return True
                #Diagonale vers en bas
                for c in range(colonnes-3):
                    for r in range(3, lignes):
                        if GRILLE[r][c] == piece and GRILLE[r-1][c+1] == piece and GRILLE[r-2][c+2] == piece and GRILLE[r-3][c+3] == piece:
                            return True


            GRILLE_inverse(GRILLE)
            running=True
            #Simple compteur
            turn=0

            #Nombre de pixels que fait la partie ou les jetons se possent
            largeur= colonnes * 80
            longuer= (lignes+1)*80
            
            #Égalité
            tie = 0

            #"Main loop" (partie ou le jeux se déroule)
            while running:
                clock.tick(60)
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        running=False
                    #Prend les coordonnées de la souris et déssine un cercle sur ces coordonnées sur un axe des abscises
                    if event.type == pygame.MOUSEMOTION:
                        pygame.draw.rect(fenetre, (30, 29, 34), (130,0, 580, 90))
                        mousex = event.pos[0]
                        if mousex <= 660 and mousex >= 170:
                            if turn == 0:
                                pygame.draw.circle(fenetre, GREEN, (mousex, 10 + int(80/2)),40)
                            else:
                                pygame.draw.circle(fenetre, YELLOW, (mousex, 10 + int(80/2)),40)
                    
                    #Ceci permet d'actualiser la fenêtre à chaque fois qu'un cercle est déssiner et la souris est bouger 
                    pygame.display.update()

                    #Prend l'événement d'une touche et prèsser 
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_m and musiqueallumer == 1:
                            pygame.mixer.music.pause()
                            musiqueallumer = musiqueallumer - 1
                        elif event.key == K_m and musiqueallumer == 0:
                            pygame.mixer.music.unpause()
                            musiqueallumer = musiqueallumer + 1
                            
                    #Ne prend en compte que les coordonnées entre des pixels que l'on lui dit (pour ne pas changer de tour losque l'on clique en dehors de la surface de jeu)
                    if event.type == pygame.MOUSEBUTTONDOWN and mousex>=160 and mousex <= 650:
                        print(event.pos)
                        if turn == 0:
                            print("C'est le tour du jouer 1")

                            mousex = event.pos[0]
                            #Colonne est la selection du juer mais avec un nombre entier pour que le jeton puise etre mise sur la zone de jeu
                            colonne = int(math.floor(mousex/80)-2)
                            print("C'est le tour du joueur 1")
                            affiche()
                            rayon = 40
                            couleur = GREEN

                            #Ceci permet de voir si la selection peut être corrcte en fonction du jeu (si posible ou pas de le placer)
                            if ligne_valide(GRILLE, colonne):
                                ligne = allez_a_la_ligne_valide(GRILLE, colonne)
                                faire_tomber_une_piece(GRILLE, ligne, colonne, 1)
                                tie = tie +1
                                
                                #Verifier si le jouer 1 a gagner
                                if verification_du_mouvement(GRILLE,1):
                                    print ("LE JOUEUR 1 a gagner!!!!")
                                    
                                    #Ouverture d'une nouvelle fenêtre lors de gagner 
                                    taille=largeur, hauteur = 850, 700
                                    fenetre = pygame.display.set_mode(taille)
                                    WHITE=(255,255,255)
                                    BLACK=(0,0,0)
                                    Grey=(60,60,60)
                                    TURC=(37,253,233)
                                    windowSurface=pygame.display.set_mode((largeur,hauteur),0,32)
                                    fenetre.blit(winner, (0, 0))

                                    police = pygame.font.SysFont('Pacifico', 50, bold=True)
                                    texte = police.render ("LE JOUEUR 1", True, (Grey))
                                    fenetre.blit (texte, (530 ,650))
                                    pygame.display.flip()
                                    
                                    #ferme tout avec un temps de délait de 5 secondes
                                    import time
                                    time.sleep(5)
                                    running == False
                                    pygame.quit()
                            #Permet de dessiner un cercle a chaque tour (change de couleur en fonction du jouer)
                            if colonne <= 5 and ligne <= 6 and GRILLE[i][colonne]!= 2:
                                pygame.draw.circle(windowSurface,YELLOW,(773,480),35,0)

                                pygame.draw.circle(fenetre, couleur, (50 + ((colonne + 2) * 80) , 550 - (ligne * 80)), rayon, 0)
                                print (pygame.mouse.get_pos())

                                position_souris=grille[0][0]


                        elif turn == 1:
                            print("C'est le tour du joueur 2 ")
            ##                pygame.draw.circle(windowSurface,GREEN,(573,480),35,0)

                            mousex = event.pos[0]
                            colonne = int(math.floor(mousex/80)-2)
                            affiche()
                            print("C'est le tour du joueur 2")
                            if ligne_valide(GRILLE, colonne):
                                ligne = allez_a_la_ligne_valide(GRILLE, colonne)
                                faire_tomber_une_piece(GRILLE, ligne,colonne,2)
                                tie = tie + 1

                                if verification_du_mouvement(GRILLE,2):
                                    print ("LE JOUEUR 2 a gagner!!!!")

                                    taille=largeur, hauteur = 850, 700
                                    fenetre = pygame.display.set_mode(taille)
                                    WHITE=(255,255,255)
                                    BLACK=(0,0,0)
                                    Grey=(60,60,60)
                                    TURC=(37,253,233)
                                    windowSurface=pygame.display.set_mode((largeur,hauteur),0,32)
                                    fenetre.blit(winner, (0, 0))

                                    police = pygame.font.SysFont('Pacifico', 50, bold=True)
                                    texte = police.render ("LE JOUEUR 2", True, (Grey))
                                    fenetre.blit (texte, (530 ,650))
                                    pygame.display.flip()

                                    import time
                                    time.sleep(5)
                                    running == False
                                    pygame.quit()

                            rayon = 40
                            couleur = YELLOW
                            if colonne <= 5 and ligne <=6 and GRILLE[i][colonne]!= 1 :
                                pygame.draw.circle(windowSurface,GREEN,(773,480),35,0)
                                pygame.draw.circle(fenetre, couleur, (50 + ((colonne + 2) * 80) , 550 - (ligne * 80)), rayon, 0)
                                print (pygame.mouse.get_pos())
                                print (tie)
                                position_souris=grille[0][0]

                        if egalite ():
                            print('egalite')

                            taille=largeur, hauteur = 290, 300
                            fenetre = pygame.display.set_mode(taille)
                            WHITE=(255,255,255)
                            BLACK=(0,0,0)
                            Grey=(60,60,60)
                            windowSurface=pygame.display.set_mode((largeur,hauteur),0,32)
                            fenetre.blit(tiegame, (0, 0))

                            pygame.display.flip()

                            import time
                            time.sleep(5)

                            pygame.quit()
                        #Permet de changer le tour des joueurs
                        turn= turn + 1
                        turn= turn % 2

    pygame.display.update()
#ferme le pygame donc ferme tout    
pygame.quit()

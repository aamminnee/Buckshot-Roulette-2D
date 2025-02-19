import pygame
import time


class Game:

    def __init__(self):
        self.playing = False
        self.manche = 1
        self.cord_millieu_atout = []
        self.tour = 0
    
    def affichage_manche(self, police, fenetre, couleur):
        manche_texte = police.render(f"Manche {self.manche}", 1, couleur)
        fenetre.blit(manche_texte, (500, 650))

    def dessine_table(self, fenetre):
        # Dessine la table de jeu
        pygame.draw.rect(fenetre, (111, 63, 77), ((0, 145), (1080, 420)), 0)
        pygame.draw.line(fenetre, (255, 255, 255), (540, 145), (540, 563), 3)
        pygame.draw.circle(fenetre, (255, 255, 255), (540, 355), 210, 3)
        pygame.draw.rect(fenetre, (192, 192, 192), ((487, 565), (106, 35)), 0)

    def dessine_emplacement_atout(self, fenetre, cord_x, cord_y, largeur, hauteur):
        # Dessine 8 emplacements pour les cartes
        espacement = 1  # Espacement entre les cartes
        cord_y_reset = cord_y - (2 * (hauteur + espacement))
        for i in range(4):
            if i <= 1:
                pygame.draw.rect(fenetre, (255, 255, 255), (cord_x, cord_y + (i * (hauteur + espacement)), largeur, hauteur), 1)
            else:
                cord_x += largeur + 1
                pygame.draw.rect(fenetre, (255, 255, 255), (cord_x, cord_y_reset + (i * (hauteur + espacement)), largeur, hauteur), 1)
                cord_x -= largeur + 1

    def dessine_ecran_vie(self, fenetre):
        pygame.draw.rect(fenetre, (192, 192, 192), ((0, 565), (61, 35)), 3)
        pygame.draw.rect(fenetre, (192, 192, 192), ((1019, 565), (61, 35)), 3)

    def affichage_tour(self, fenetre, couleur):
        if self.tour == 0:
            pygame.draw.rect(fenetre, (couleur), ((170, 75), (345, 50)), 2)
        elif self.tour == 1:
            pygame.draw.rect(fenetre, (couleur), ((566, 75), (345, 50)), 2)
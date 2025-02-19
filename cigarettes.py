import pygame, random

class Cigarette:

    def __init__(self):
        self.image = pygame.image.load("./images/cigarette.png")
        
    def fumer(self, vie_joueur):
        X_aleatoire = random.randint(1, 2)
        vie_joueur[X_aleatoire] += 1
        return vie_joueur
    
    def affiche_cigarette(self, fenetre):
        fenetre.blit(self.image, (350, 200))

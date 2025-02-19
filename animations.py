import pygame
from arme import Arme

arme = Arme()

class Animations:

    def __init__(self):
        self.animation_tir = []
        for i in range(1, 10):
            image_chemin = f"./fumées/fumee{i}.png"
            image = pygame.image.load(image_chemin)
            image = pygame.transform.scale(image, (50, 50))
            self.animation_tir.append(image)
        self.animation_tir_inverse = []
        for j in range(1,  10):
            image_chemin_inverse = f"./fumées inversées/fumee{j}_inverse.png"
            image_inverse = pygame.image.load(image_chemin_inverse)
            image_inverse = pygame.transform.scale(image_inverse, (50, 50))
            self.animation_tir_inverse.append(image_inverse)
        self.index_image = 0
        self.duree_affichage_image = 20
        self.temps_prochain_affichage = 0
        self.animation_en_cours = False

    def demarrer_animation(self):
        if not self.animation_en_cours:
            self.animation_en_cours = True
            self.temps_prochain_affichage = pygame.time.get_ticks() + self.duree_affichage_image

    def afficher_animation(self, fenetre):
        if self.animation_en_cours:
            if arme.detect_tirer_j1():
                fenetre.blit(self.animation_tir_inverse[self.index_image], (415, 310))
                arme.affichage_shotgun_miroir(fenetre)
            if arme.detect_tirer_j2():
                fenetre.blit(self.animation_tir[self.index_image], (615, 310))
                arme.affichage_shotgun(fenetre)
            t_actuel = pygame.time.get_ticks()
            if t_actuel >= self.temps_prochain_affichage:
                self.index_image += 1
                if self.index_image >= len(self.animation_tir) or self.index_image >= len(self.animation_tir):
                    self.index_image = 0
                    self.animation_en_cours = False
                self.temps_prochain_affichage = t_actuel + self.duree_affichage_image


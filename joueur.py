import pygame
import time

class Joueur:

    def __init__(self):
        self.vie = 6
        self.pseudo = ""
        self.inventaire = {}
        self.clignotement = False
        self.last_toggle_time = 0
        self.ecrit = False
        self.valider_pseudo = False
        self.affiche = False

    def dessine_vie(self, fenetre, cord_x):
        for _ in range(self.vie):
            if self.vie == 6:
                pygame.draw.rect(fenetre, (100, 255, 50), ((cord_x, 569), (8, 27)), 0)
            elif self.vie < 6:
                pygame.draw.rect(fenetre, (255, 255, 255), ((cord_x, 569), (8, 27)), 0)
            cord_x += 9

    def retirer_vie(self, balle):
        self.vie -= balle
        print(self.vie)

    def detect_gagnant_manche(self, pseudo, vie, fenetre, police, couleur):
        if vie == 0:
            gagnant = police.render(f"{pseudo} a gagné la manche !", 1, couleur)
            fenetre.blit(gagnant, (410, 620))
            return True
        
    def vie_clignote(self, fenetre, cord_x):
        if self.vie == 1:
            pygame.draw.rect(fenetre, (255, 0, 0), ((cord_x, 569), (8, 27)), 0)
            current_time = time.time()
            if current_time - self.last_toggle_time > 0.5:
                self.clignotement = not self.clignotement
                self.last_toggle_time = current_time

            if self.clignotement:
                pygame.draw.rect(fenetre, (0, 0, 0), ((cord_x, 569), (8, 27)), 0)

    def entrer_utilisateur(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if len(self.pseudo) > 0:
                    self.affiche = True
            elif event.key == pygame.K_BACKSPACE:
                if len(self.pseudo) > 0:
                    self.pseudo = self.pseudo[:-1]
            else:
                if len(self.pseudo) < 6:
                    self.pseudo += event.unicode
    
    def afficher_pseudo(self, fenetre, police, couleur, cord_x, cord_y):
        if self.affiche:
            pseudo = police.render(self.pseudo, 1, couleur)
            fenetre.blit(pseudo, (cord_x, cord_y))
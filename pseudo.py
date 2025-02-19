import pygame


class Pseudo:

    def __init__(self):
        self.contrat = pygame.image.load("./images/contrat_prenom.png")
        self.playing = False
        self.rect_entrer = pygame.Rect(900, 649, 70, 50)

    def dessine_contrat(self, fenetre):
        if self.playing:
            cord = [93, 586]
            for i in range(2):
                fenetre.blit(self.contrat, (cord[i], 101))
                # pygame.draw.rect(fenetre, (0, 0, 0), ((255, 535), (225, 60)), 1)
                # pygame.draw.rect(fenetre, (0, 0, 0), ((745, 535), (225, 60)), 1)
        
    def consigne(self, fenetre, police, couleur):
        if self.playing:
            cord = [103, 596] 
            for i in range(2):
                entrer = police.render(f"Le joueur {i + 1} signez le contrat: ", 1, couleur)
                fenetre.blit(entrer, (cord[i], 77))

    def afficher_pseudo(self, fenetre, police, couleur, cord_x, cord_y, pseudo):
        pseudo = police.render(pseudo, 1, couleur)
        fenetre.blit(pseudo, (cord_x, cord_y))

    def valider(self, fenetre, police, couleur):
        if self.playing:
            valider_text = police.render("valider", 1, couleur)
            fenetre.blit(valider_text, (906, 661))
            pygame.draw.rect(fenetre, couleur, self.rect_entrer, 4, 20)
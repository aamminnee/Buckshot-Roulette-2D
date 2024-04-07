import pygame, random, math

fenetre = pygame.display.set_mode((1080, 720))

class Arme:

    def __init__(self, vie_joueur, chargeur):
        self.shotgun = pygame.image.load("./images/shotgun.png")
        self.shotgun = pygame.transform.scale(self.shotgun, (170, 50))
        self.blanche = pygame.image.load("./images/blanche.png")
        self.blanche = pygame.transform.scale(self.blanche, (69, 45))
        self.blanche = pygame.transform.rotate(self.blanche, 90)
        self.rouge = pygame.image.load("./images/rouge.png")        
        self.rouge = pygame.transform.scale(self.rouge, (69, 45))
        self.rouge = pygame.transform.rotate(self.rouge, 90)
        self.vie_joueur = vie_joueur
        self.chargeur = chargeur

    def recharge(self):
        if len(self.chargeur) == 0 or 0 in self.vie_joueur:
            self.chargeur = []
            capacite_chargeur = random.randint(2, 8)
            if capacite_chargeur == 2:
                nb_balles_rouges = 1
            else:
                nb_balles_rouges = random.uniform(capacite_chargeur / 4, float(capacite_chargeur // 2))
            print("nb: ", nb_balles_rouges, math.ceil(nb_balles_rouges))
            self.chargeur = self.chargeur + [1] * math.ceil(nb_balles_rouges) + [0] * (capacite_chargeur - math.ceil(nb_balles_rouges))
            random.shuffle(self.chargeur)
            print(self.chargeur)
        return self.chargeur
    
    def tire(self, cible):
        self.vie_joueur[cible] -= self.chargeur.pop(-1)
        return self.chargeur, self.vie_joueur

    def affichage_blanche(self, fenetre, cord):
        fenetre.blit(self.blanche, cord)

    def affichage_rouge(self, fenetre, cord):
        fenetre.blit(self.rouge, cord)

    def affichage_shotgun(self, fenetre):
        fenetre.blit(self.shotgun, (460, 300))

    def affichage_chargeur(self):
        pos_y_b = 426
        pos_y_r = 426 + (12 * self.chargeur.count(0)) + 5
        nb_balles_blanche = self.chargeur.count(0) 
        for i in range(len(self.chargeur)):
            if i <= nb_balles_blanche - 1:
                self.affichage_blanche(fenetre, (529, pos_y_b))
                pos_y_b += 12
            else:
                self.affichage_rouge(fenetre, (529, pos_y_r))
                pos_y_r += 12
        
                
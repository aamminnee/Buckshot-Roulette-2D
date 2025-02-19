import pygame, random, math

fenetre = pygame.display.set_mode((1080, 720))

class Arme:

    def __init__(self):
        self.shotgun = pygame.image.load("./images/shotgun.png")
        self.shotgun = pygame.transform.scale(self.shotgun, (170, 50))
        self.shotgun_inverse = pygame.image.load("./images/shotgun_miroir.png")
        self.shotgun_inverse = pygame.transform.scale(self.shotgun_inverse, (170, 50))
        self.viseur = pygame.image.load("./images/viseur.png")
        self.viseur = pygame.transform.scale(self.viseur, (50, 50))
        self.chargeur = []
        self.force_recharge = False
        self.stop_tir = False

    def recharge(self):
        if len(self.chargeur) == 0 or self.force_recharge:
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
    
    def tire(self):
        return self.chargeur.pop()

    def affichage_balle(self, fenetre, cord, couleur):
        pygame.draw.rect(fenetre, couleur, (cord, (8, 25)), 0)
        pygame.draw.rect(fenetre, (0, 0, 0), ((cord[0], cord[-1] - 8), (8, 8)), 0)

    def affichage_shotgun(self, fenetre):
        fenetre.blit(self.shotgun, (455, 330))

    def affichage_shotgun_miroir(self, fenetre):
        fenetre.blit(self.shotgun_inverse, (455, 330))

    def affichage_chargeur(self):
        pos_x_b = 492
        pos_x_r = 492 + (12 * self.chargeur.count(0)) + 5
        nb_balles_blanche = self.chargeur.count(0) 
        for i in range(len(self.chargeur)):
            if i <= nb_balles_blanche - 1:
                self.affichage_balle(fenetre, (pos_x_b, 574), (255, 255, 255))
                pos_x_b += 12
            else:
                self.affichage_balle(fenetre, (pos_x_r, 574), (255, 0, 0))
                pos_x_r += 12
        
    def bouton_viser(self, fenetre):
        pos_x = 460
        for _ in range(2):
            fenetre.blit(self.viseur, (pos_x, 75))
            pos_x += 112

    def detect_tirer_j1(self):
        if pygame.Rect(460, 75, 50, 50).collidepoint(pygame.mouse.get_pos()) and not self.stop_tir:
            return True
        
    def detect_tirer_j2(self):
        if pygame.Rect(576, 75, 50, 50).collidepoint(pygame.mouse.get_pos()) and not self.stop_tir:
            return True
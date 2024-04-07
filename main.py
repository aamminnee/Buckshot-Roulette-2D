import pygame
from menu import Menu
from game import Game
from arme import Arme
from cigarettes import Cigarette

pygame.init()

fenetre = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Buckshot Roulette")

BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
NOIR = (0, 0, 0)

background = pygame.image.load("./images/background.png")
police = pygame.font.SysFont("Times New Roman", 20)
jouer_texte = police.render("Jouer", 1, BLANC)
regles_texte = police.render("Règles du jeu", 1, BLANC)
quitter_texte = police.render("Quitter le jeu", 1, BLANC)

# Créez une instance de la classe Menu
menu = Menu()
game = Game()
arme = Arme((3, 3), [])
cigarettes = Cigarette() 

def est_survole(x, y, largeur, hauteur):
    souris_x, souris_y = pygame.mouse.get_pos()
    return x < souris_x < x + largeur and y < souris_y < y + hauteur

run = True
while run:
    fenetre.blit(background, (0, 0))

    if est_survole(520, 475, jouer_texte.get_width(), jouer_texte.get_height()):
        jouer_texte = police.render("Jouer", 1, ROUGE)
    else:
        jouer_texte = police.render("Jouer", 1, BLANC)
    if est_survole(490, 510, regles_texte.get_width(), regles_texte.get_height()):
        regles_texte = police.render("Règles du jeu", 1, ROUGE)
    else:
        regles_texte = police.render("Règles du jeu", 1, BLANC)
    if est_survole(480, 545, quitter_texte.get_width(), quitter_texte.get_height()):
        quitter_texte = police.render("Quitter le jeu", 1, ROUGE)
    else:
        quitter_texte = police.render("Quitter le jeu", 1, BLANC)

    fenetre.blit(jouer_texte, (520, 475))
    fenetre.blit(regles_texte, (490, 510))
    fenetre.blit(quitter_texte, (490, 545))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if pygame.Rect(520, 475, jouer_texte.get_width(), jouer_texte.get_height()).collidepoint(pygame.mouse.get_pos()):
                game.playing = True
            elif pygame.Rect(490, 510, regles_texte.get_width(), regles_texte.get_height()).collidepoint(pygame.mouse.get_pos()):
                menu.flou_playing = True
                menu.regle_playing = True
                menu.retour_playing = True
            elif pygame.Rect(480, 545, quitter_texte.get_width(), quitter_texte.get_height()).collidepoint(pygame.mouse.get_pos()):
                run = False
            elif menu.retour_rect.collidepoint(pygame.mouse.get_pos()):
                menu.flou_playing = False
                menu.regle_playing = False
                menu.retour_playing = False
                game.playing = False
                arme.chargeur = []
                
    if menu.flou_playing:
        menu.flou_bg(fenetre)
    if menu.regle_playing:
        menu.affichage_regle(fenetre)
    if menu.retour_playing:
        menu.bouton_retour(fenetre)
    if game.playing:
        game.affichage_fond_noir(fenetre)
        game.affichage_table(fenetre)
        arme.recharge()
        arme.affichage_chargeur()
        arme.affichage_shotgun(fenetre)
        cigarettes.affiche_cigarette(fenetre)
        menu.retour_playing = True
        menu.bouton_retour(fenetre)

    pygame.display.update()

pygame.quit()

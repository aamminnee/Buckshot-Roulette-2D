import pygame
from joueur import Joueur
from menu import Menu
from game import Game
from arme import Arme
from cigarettes import Cigarette
from pseudo import Pseudo
from sons import SoundManager
from animations import Animations
import time

pygame.init()

fenetre = pygame.display.set_mode((1080, 720))
pygame.display.set_caption("Buckshot Roulette")

BLANC = (255, 255, 255)
ROUGE = (255, 0, 0)
ROUGE_C = (253, 20, 39)
NOIR = (0, 0, 0)
GRIS = (192, 192, 192)

background = pygame.image.load("./images/background.png")
police = pygame.font.SysFont("Times New Roman", 20)
police1 = pygame.font.SysFont("Times New Roman", 40)
jouer_texte = police.render("Jouer", 1, BLANC)
regles_texte = police.render("Règles du jeu", 1, BLANC)
quitter_texte = police.render("Quitter le jeu", 1, BLANC)
temps_affichage_message = None

# Créez une instance des différentes classes:
menu = Menu()
game = Game()
arme = Arme()
j1, j2 = Joueur(), Joueur()
cigarettes = Cigarette()
son = SoundManager()
pseudo = Pseudo()
animations = Animations()

son.jouer_musique_menu()


def est_survole(x, y, largeur, hauteur):
    souris_x, souris_y = pygame.mouse.get_pos()
    return x < souris_x < x + largeur and y < souris_y < y + hauteur


run = True
last_shot_time = 0
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
            current_time = time.time()
            if current_time - last_shot_time >= 1.0:
                if arme.detect_tirer_j1() and menu.retour_playing and not pseudo.playing:
                    balle = arme.tire()
                    j1.retirer_vie(balle)
                    if balle == 0:
                        if arme.detect_tirer_j2():
                            game.tour = 1
                        else:
                            game.tour = 0
                        son.jouer_son("click")
                        son.jouer_son("douille_tombe")
                    elif balle == 1:
                        if arme.detect_tirer_j2():
                            game.tour = 0
                        else:
                            game.tour = 1
                        animations.demarrer_animation()
                        son.jouer_son("tir")
                        son.jouer_son("douille_tombe")
                    last_shot_time = current_time
                if arme.detect_tirer_j2() and menu.retour_playing and not pseudo.playing:
                    balle = arme.tire()
                    j2.retirer_vie(balle)
                    if balle == 0:
                        if arme.detect_tirer_j1():
                            game.tour = 0
                        else:
                            game.tour = 1
                        son.jouer_son("click")
                        son.jouer_son("douille_tombe")
                    elif balle == 1:
                        if arme.detect_tirer_j1():
                            game.tour = 1
                        else:
                            game.tour = 0
                        animations.demarrer_animation()
                        son.jouer_son("tir")
                        son.jouer_son("douille_tombe")
                    last_shot_time = current_time
            if son.couper_rect.collidepoint(pygame.mouse.get_pos()):
                if not pseudo.playing and not game.playing and not menu.retour_playing:
                    son.jouer_son("click")
                    son.couper_son()
            if pygame.Rect(520, 475, jouer_texte.get_width(), jouer_texte.get_height()).collidepoint(pygame.mouse.get_pos()):
                if not pseudo.playing and not menu.playing:
                    son.jouer_son("click")
                    pseudo.playing = True
                    menu.flou_playing = True
                    menu.retour_playing = True
            elif pygame.Rect(490, 510, regles_texte.get_width(), regles_texte.get_height()).collidepoint(pygame.mouse.get_pos()):
                if not pseudo.playing and not menu.playing:
                    son.jouer_son("click")
                    menu.flou_playing = True
                    menu.regle_playing = True
                    menu.retour_playing = True
                    menu.playing = True
            elif pygame.Rect(480, 545, quitter_texte.get_width(), quitter_texte.get_height()).collidepoint(pygame.mouse.get_pos()):
                if not pseudo.playing and not menu.playing:
                    run = False
            elif pseudo.rect_entrer.collidepoint(pygame.mouse.get_pos()):
                if pseudo.playing and not game.playing:
                    son.jouer_son("click")
                    game.playing = True
                    pseudo.playing = False
                    if son.musique_menu_playing:
                        son.arreter_musique_menu()
            elif menu.retour_rect.collidepoint(pygame.mouse.get_pos()):
                if pseudo.playing or game.playing or menu.playing:
                    son.jouer_son("click")
                    menu.flou_playing = False
                    menu.regle_playing = False
                    menu.retour_playing = False
                    pseudo.playing = False
                    game.playing = False
                    menu.playing = False
                    j1.ecrit = False
                    j2.ecrit = False
                    j1.valider_pseudo = False
                    j2.valider_pseudo = False 
                    arme.chargeur = []
                    game.manche = 1
                    game.tour = 0
                    j1.vie, j2.vie = 6, 6
                    j1.pseudo, j2.pseudo = "", ""
                    """if not son.musique_menu_playing:
                        son.jouer_musique_menu()
                    son.musique_playing = son.musique_playing"""
            if pygame.Rect(255, 535, 225, 60).collidepoint(pygame.mouse.get_pos()) and not j2.ecrit:
                j1.ecrit = True
            if pygame.Rect(745, 535, 225, 60).collidepoint(pygame.mouse.get_pos()) and not j1.ecrit:
                j2.ecrit = True
        elif event.type == pygame.KEYDOWN and j1.ecrit and not j1.valider_pseudo:
            if pseudo.playing and not j2.ecrit:
                j1.entrer_utilisateur(event)
            if event.key == pygame.K_RETURN and len(j1.pseudo) > 0:
                j1.ecrit = False
                j1.valider_pseudo = True
        elif event.type == pygame.KEYDOWN and j2.ecrit and not j2.valider_pseudo:
            if pseudo.playing and not j1.ecrit:
                j2.entrer_utilisateur(event)
            if event.key == pygame.K_RETURN and len(j2.pseudo) > 0:
                j2.ecrit = False
                j2.valider_pseudo = True
    son.affichage_couper_son(fenetre)            
    if menu.flou_playing:
        menu.flou_bg(fenetre)
    if menu.regle_playing:
        menu.affichage_regle(fenetre)
    if menu.retour_playing:
        menu.bouton_retour(fenetre)
    if pseudo.playing:
        menu.flou_bg(fenetre)
        pseudo.dessine_contrat(fenetre)
        menu.bouton_retour(fenetre)
        pseudo.consigne(fenetre, police, BLANC)
        if est_survole(255, 535, 225, 60) and not j1.ecrit and not j1.valider_pseudo:
            pygame.draw.rect(fenetre, (GRIS), ((257, 539), (212, 55)), 100)
        if est_survole(745, 535, 225, 60) and not j2.ecrit and not j2.valider_pseudo:
            pygame.draw.rect(fenetre, (GRIS), ((750, 539), (212, 55)), 100)
        pseudo.afficher_pseudo(fenetre, police1, NOIR, 257, 535, j1.pseudo)
        pseudo.afficher_pseudo(fenetre, police1, NOIR, 750, 535, j2.pseudo)
        if j1.valider_pseudo and j2.valider_pseudo:
            if est_survole(900, 649, 70, 50):
                pseudo.valider(fenetre, police, ROUGE)
            else:
                pseudo.valider(fenetre, police, BLANC)
    if game.playing:
        fenetre.fill((0, 0, 0))
        game.dessine_table(fenetre)
        game.dessine_emplacement_atout(fenetre, 30, 165, 120, 70)
        game.dessine_emplacement_atout(fenetre, 810, 165, 120, 70)
        game.dessine_emplacement_atout(fenetre, 30, 393, 120, 70)
        game.dessine_emplacement_atout(fenetre, 810, 393, 120, 70)
        game.affichage_manche(police,  fenetre, BLANC)
        game.dessine_ecran_vie(fenetre)
        j1.afficher_pseudo(fenetre, police1, ROUGE_C, 175, 80)
        j2.afficher_pseudo(fenetre, police1, ROUGE_C, 712, 80)
        game.affichage_tour(fenetre, ROUGE_C)
        if arme.chargeur == []:
            son.jouer_son("recharge")
        arme.recharge()
        arme.affichage_chargeur()
        menu.retour_playing = True
        menu.bouton_retour(fenetre)
        arme.bouton_viser(fenetre)
        animations.afficher_animation(fenetre)
        j1.dessine_vie(fenetre, 4)
        j2.dessine_vie(fenetre, 1023)
        if j1.detect_gagnant_manche(j1.pseudo, j2.vie, fenetre, police, BLANC) or \
           j2.detect_gagnant_manche(j2.pseudo, j1.vie, fenetre, police, BLANC):
            if temps_affichage_message is None:
                temps_affichage_message = pygame.time.get_ticks()
                arme.force_recharge = True
                arme.recharge()
                arme.force_recharge = False
                arme.stop_tir = True
            elif pygame.time.get_ticks() - temps_affichage_message >= 3000:
                j1.vie, j2.vie = 6, 6
                temps_affichage_message = None
                game.manche += 1
                arme.stop_tir = False
        if arme.detect_tirer_j1():
            arme.affichage_shotgun_miroir(fenetre)
        if arme.detect_tirer_j2():
            arme.affichage_shotgun(fenetre)
        if j1.vie == 1:
            j1.vie_clignote(fenetre, 4)
        if j2.vie == 1:
            j2.vie_clignote(fenetre, 1023)
    if game.manche > 3:
        game.manche = 1
        game.playing = False
        menu.flou_playing = False
        menu.retour_playing = False
        ecrire1 = False
        ecrire2 = False
        fin_pseudo1 = False
        fin_pseudo2 = False
        son.jouer_musique_menu()

    pygame.display.update()

pygame.quit()

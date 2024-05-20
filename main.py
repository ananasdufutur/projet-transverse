# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame
import math
import time
from pygame.locals import *
pygame.init()
from game import Game

from pygame.locals import K_RETURN, K_SPACE, KEYDOWN, KEYUP, QUIT, RESIZABLE








# Fill background
fenetre = pygame.display.set_mode((1000,600), RESIZABLE)
pygame.display.set_caption('jeu de bombarde')


background=pygame.image.load('assets/1200px-SSBU-Pokémon_Stadium_2.webp')

banner=pygame.image.load("assets/1595041602_Kanji_tatsumi.png")
#banner=pygame.transform.scale(banner)
banner_rect=banner.get_rect()
banner_rect.x=math.ceil(fenetre.get_width()/3.2)

play_button=pygame.image.load('assets/1000002362-removebg-preview.png')
play_button=pygame.transform.scale(play_button,(600,300))
play_button_rect=play_button.get_rect()
play_button_rect.x=math.ceil(fenetre.get_width()/4.95)
play_button_rect.y=math.ceil(fenetre.get_height()/1.5)

game = Game()
b=0
a=1
fenetre.blit(background, (0,0))
continuer = 1
while continuer:
    if game.is_playing:
        continuer=game.update(fenetre,a,continuer)
    else:
        fenetre.blit(banner,banner_rect)
        fenetre.blit(play_button,play_button_rect)
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
        elif event.type==pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()


    pygame.display.flip()
pygame.quit()

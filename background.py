import pygame
from pygame.locals import *
import sys
import os

from player import *

                    
# define display surface			
W, H = 960, 540
HW, HH = W / 2, H / 2
AREA = W * H

os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

# setup pygame
pygame.init()
CLOCK = pygame.time.Clock()
DS = pygame.display.set_mode((W, H))
FPS = 120
#chargement de l'image background
bkgd = pygame.image.load("assets/background.jpg").convert()
x = 0
#chargement du personnage
perso = pygame.image.load("assets/perso.png").convert()
perso_x = 0
perso_y = 480
DS.blit(perso, (perso_x, perso_y))
pygame.display.flip()

pygame.mixer.music.load("assets/music.wav")
pygame.mixer.music.play()

#def spawn():
     
    

DS.blit(perso, (perso_x, perso_y))     
# main loop
pygame.key.set_repeat(1,20)
while True:
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()
        if event.type == KEYDOWN:
            if event.key == K_RIGHT:
                perso_x = 0
                if perso_x <= 960:
                    perso = pygame.image.load("assets/right.png").convert_alpha()
                    perso_x += 200
            if event.key == K_SPACE:
                perso_y = 480
                if perso_y <= 480:
                    perso = pygame.image.load("assets/jump.png").convert_alpha()
                    perso_y += 5
    pygame.display.flip()
    rel_x = x % bkgd.get_rect().width
    DS.blit(bkgd, (rel_x - bkgd.get_rect().width, 0))
    if rel_x < W:
        DS.blit(bkgd, (rel_x, 0))
    x -= 1
    
    #DS.display(flip)
    DS.blit(perso, (perso_x, perso_y))
    
    pygame.display.update()
    CLOCK.tick(FPS)
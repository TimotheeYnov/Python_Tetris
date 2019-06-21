import pygame
from pygame.locals import *

pygame.init ()

window = pygame.display.set_mode((640, 480),RESIZABLE)

fond = pygame.image.load("valentin1.png").convert()
window.blit(fond, (0,0))

pygame.display.flip()

continuer = 1

while continuer:
        continuer = int(input())
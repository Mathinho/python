import pygame, sys
from pygame.locals import *

GRAY = (200, 200, 200)
RED = (255, 0, 0)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Python Game')
DISPLAYSURF.fill(GRAY)
pygame.draw.ellipse(DISPLAYSURF, RED, (300, 250, 40, 80), 1)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
import pygame, sys
from pygame.locals import *

GRAY = (200, 200, 200)
RED = (255, 0, 0)

pygame.init()

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((600, 400))
pygame.display.set_caption('Python Game')

image = pygame.image.load('test.png')
imageX = 10
imageY = 10
direction = 'right'

while True:
    DISPLAYSURF.fill(GRAY)

    if direction == 'right':
        imageX += 5
    if imageX == 280:
        direction = 'down'
    elif direction == 'down':
        imageY += 5
    if imageY == 220:
        direction = 'left'
    elif direction == 'left':
        imageX -= 5
    if imageX == 10:
        direction = 'up'
    elif direction == 'up':
        imageY -= 5
    if imageY == 10:
        direction = 'right'

    DISPLAYSURF.blit(image, (imageX, imageY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
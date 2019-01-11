#disable various wrong error messages
#pylint:disable=E1101
#pylint:disable=E0602
#pylint:disable=W0614
import pygame, sys
from pygame.locals import *

GRAY = (200, 200, 200)
RED = (255, 0, 0)

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((1200, 1000))
pygame.NOFRAME
pygame.display.set_caption('Martas Quest')

image = pygame.image.load('test.png')
image = pygame.transform.scale(image, (800, 200))
imageX = 1
imageY = 1
direction = 'right'

while True:
    DISPLAYSURF.fill(GRAY)

    #if direction == 'right':
    #    imageX += 2
    #    if imageX == 395:
    #        direction = 'down'
    #elif direction == 'down':
    #    imageY += 2
    #    if imageY == 801:
    #        direction = 'left'
    #elif direction == 'left':
    #    imageX -= 2
    #    if imageX == 1:
    #        direction = 'up'
    #elif direction == 'up':
    #    imageY -= 2
    #    if imageY == 1:
    #        direction = 'right'
    key = pygame.key.get_pressed()

    if key [pygame.K_LEFT]:
        imageX -= 1
    elif key [pygame.K_RIGHT]:
        imageX += 1
    elif key [pygame.K_DOWN]:
        imageY += 1
    elif key [pygame.K_UP]:
        imageY -= 1

    DISPLAYSURF.blit(image, (imageX, imageY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
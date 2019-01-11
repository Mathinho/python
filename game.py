#disable various wrong error messages
#pylint:disable=E1101
#pylint:disable=E0602
#pylint:disable=W0614
import pygame, sys
from pygame.locals import *

GRAY = (200, 200, 200)
RED = (200, 0, 0)

pygame.init()

FPS = 60 # frames per second setting
fpsClock = pygame.time.Clock()

#define window size
DISPLAYSURF = pygame.display.set_mode((1200, 1000))
pygame.NOFRAME
pygame.display.set_caption('Martas Quest')

#load various images
imageLEFT = pygame.image.load('marioLEFT.png')
imageLEFT = pygame.transform.scale(imageLEFT, (80, 94))
imageRIGHT = pygame.image.load('marioRIGHT.png')
imageRIGHT = pygame.transform.scale(imageRIGHT, (80, 94))
imageLAST = pygame.image.load('marioRIGHT.png')
imageLAST = pygame.transform.scale(imageRIGHT, (80, 94))
imageX = 1
imageY = 1

#load background music
theme = pygame.mixer.music.load('SuperMarioBros.ogg')
pygame.mixer.music.play()

while True:
    DISPLAYSURF.fill(GRAY)

    #get keyboard to move character
    key = pygame.key.get_pressed()
    if key [pygame.K_LEFT]:
        DISPLAYSURF.blit(imageLEFT, (imageX, imageY))
        imageX -= 1
        imageLAST = imageLEFT
    elif key [pygame.K_RIGHT]:
        DISPLAYSURF.blit(imageRIGHT, (imageX, imageY))
        imageX += 1
        imageLAST = imageRIGHT
    elif key [pygame.K_DOWN]:
        DISPLAYSURF.blit(imageRIGHT, (imageX, imageY))
        imageY += 1
        imageLAST = imageRIGHT
    elif key [pygame.K_UP]:
        DISPLAYSURF.blit(imageRIGHT, (imageX, imageY))
        imageY -= 1
        imageLAST = imageRIGHT

    if imageX >= imageY >= 100:
        DISPLAYSURF.fill(RED)

    #show character
    DISPLAYSURF.blit(imageLAST, (imageX, imageY))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
import pygame

CASA_1_W, CASA_1_H = 200, 200
CASA_1 = pygame.image.load('images/buildings2.png')
CASA_1 = pygame.transform.scale(CASA_1, (CASA_1_W, CASA_1_H))

CASA_3 = pygame.image.load('images/buildings3.png')
CASA_3 = pygame.transform.scale(CASA_3, (CASA_1_W, CASA_1_H))

CASA_4 = pygame.image.load('images/buildings4.png')
CASA_4 = pygame.transform.scale(CASA_4, (CASA_1_W, CASA_1_H))

CASA_BIG = pygame.image.load('images/buildings5.png')
CASA_BIG = pygame.transform.scale(CASA_BIG, (CASA_1_W+50, CASA_1_H+50))
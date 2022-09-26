import pygame
from load_things import CASA_1, CASA_3, CASA_4, CASA_BIG


WIDTH, HEIGHT = 1280, 720
PAOLO_WIDTH, PAOLO_HEIGHT = 45, 50
FPS = 60
VEL = 3

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

GRASS = pygame.image.load('images/grass.jpg')
GRASS = pygame.transform.scale(GRASS, (WIDTH, HEIGHT))

PROT_L = pygame.transform.scale(pygame.image.load('images/pers_left.PNG'), (PAOLO_WIDTH, PAOLO_HEIGHT))
PROT_R = pygame.transform.scale(pygame.image.load('images/pers_right.PNG'), (PAOLO_WIDTH, PAOLO_HEIGHT))
PROT_U = pygame.transform.scale(pygame.image.load('images/pers_back.PNG'), (PAOLO_WIDTH, PAOLO_HEIGHT))
PROT_D = pygame.transform.scale(pygame.image.load('images/pers_front.PNG'), (PAOLO_WIDTH, PAOLO_HEIGHT))
PROT = PROT_D

global current_prot_dir
current_prot_dir = PROT_D


def draw_window(paolo, casa_1, casa_3, casa_4, casa_big):
    WIN.blit(GRASS, (0, 0))
    WIN.blit(CASA_1, (casa_1.x, casa_1.y))
    WIN.blit(CASA_3, (casa_3.x, casa_3.y))
    WIN.blit(CASA_4, (casa_4.x, casa_4.y))
    WIN.blit(CASA_BIG, (casa_big.x, casa_big.y))

    WIN.blit(current_prot_dir, (paolo.x, paolo.y))

    pygame.display.update()


def handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_LEFT]:  # left
        globals()['current_prot_dir'] = PROT_L
        yellow.x -= VEL
    if keys_pressed[pygame.K_RIGHT]: # right
        globals()['current_prot_dir'] = PROT_R
        yellow.x += VEL
    if keys_pressed[pygame.K_UP]:  # up
        globals()['current_prot_dir'] = PROT_U
        yellow.y -= VEL
    if keys_pressed[pygame.K_DOWN]:  # down
        globals()['current_prot_dir'] = PROT_D
        yellow.y += VEL


if __name__ == '__main__':



    clock = pygame.time.Clock()
    run = True

    paolo = pygame.Rect(WIDTH//3, HEIGHT//2, PAOLO_WIDTH, PAOLO_HEIGHT)
    casa_1 = pygame.Rect(50, 100, 200, 200)
    casa_3 = pygame.Rect(270, 50, 200, 200)
    casa_4 = pygame.Rect(500, 100, 200, 200)
    casa_big = pygame.Rect(900, 100, 250, 250)

    while run:
        clock.tick(FPS)
        draw_window(paolo, casa_1, casa_3, casa_4, casa_big)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed, paolo)
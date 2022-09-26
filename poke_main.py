import pygame
from load_things import CASA_1, CASA_3, CASA_4, CASA_BIG


WIDTH, HEIGHT = 1280, 720
HOUSE_W, HOUSE_H = 720, 720
PAOLO_WIDTH, PAOLO_HEIGHT = 45, 50
FPS = 60
VEL = 3
BLACK = (0, 0, 0)

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

GRASS = pygame.image.load('images/grass.jpg')
GRASS = pygame.transform.scale(GRASS, (WIDTH, HEIGHT))

HOUSE = pygame.image.load('images/arancione.jpg')
HOUSE = pygame.transform.scale(HOUSE, (HOUSE_W, HOUSE_H))

PORTA = pygame.image.load('images/porta_interna.jpg')
PORTA = pygame.transform.scale(PORTA, (60, 40))

PROT_L = pygame.transform.scale(pygame.image.load('images/pers_left.PNG'), (PAOLO_WIDTH, PAOLO_HEIGHT))
PROT_R = pygame.transform.scale(pygame.image.load('images/pers_right.PNG'), (PAOLO_WIDTH, PAOLO_HEIGHT))
PROT_U = pygame.transform.scale(pygame.image.load('images/pers_back.PNG'), (PAOLO_WIDTH, PAOLO_HEIGHT))
PROT_D = pygame.transform.scale(pygame.image.load('images/pers_front.PNG'), (PAOLO_WIDTH, PAOLO_HEIGHT))
PROT = PROT_D

global current_prot_dir
global level
current_prot_dir = PROT_D
level = 1


def draw_window_level_1(paolo, casa_1, casa_3, casa_4, casa_big):
    WIN.blit(GRASS, (0, 0))
    WIN.blit(CASA_1, (casa_1.x, casa_1.y))
    WIN.blit(CASA_3, (casa_3.x, casa_3.y))
    WIN.blit(CASA_4, (casa_4.x, casa_4.y))
    WIN.blit(CASA_BIG, (casa_big.x, casa_big.y))
    WIN.blit(current_prot_dir, (paolo.x, paolo.y))
    pygame.display.update()


def draw_window_level_3(paolo, porta):

    WIN.fill(BLACK)
    WIN.blit(HOUSE, (560, 0))
    WIN.blit(PORTA, (porta.x, porta.y))

    WIN.blit(current_prot_dir, (paolo.x, paolo.y))
    pygame.display.update()


def handle_movement(keys_pressed, paolo, lista_case, ingresso_porta, porta_interna):

    input_x, input_y = 0, 0


    if keys_pressed[pygame.K_LEFT]:
        input_x = -1
        globals()['current_prot_dir'] = PROT_L
    if keys_pressed[pygame.K_RIGHT]:
        input_x = 1
        globals()['current_prot_dir'] = PROT_R
    if keys_pressed[pygame.K_UP]:
        input_y = -1
        globals()['current_prot_dir'] = PROT_U
    if keys_pressed[pygame.K_DOWN]:
        input_y = 1
        globals()['current_prot_dir'] = PROT_D

    if abs(input_x) == 1 and abs(input_y) == 1:
        input_x = 0
        input_y = 0

    mov_x = input_x * VEL
    mov_y = input_y * VEL

    paolo.x += mov_x
    paolo.y += mov_y

    if level == 1:
        for casa in lista_case:
            if paolo.colliderect(casa):
                paolo.x -= mov_x
                paolo.y -= mov_y

        if paolo.colliderect(ingresso_porta):
            globals()['level'] = 3
            paolo.x = porta_interna.x + 8
            paolo.y = porta_interna.y - 90

    if level == 3:
        if paolo.colliderect(porta_interna):
            globals()['level'] = 1
            paolo.x = ingresso_porta.x - 18
            paolo.y = ingresso_porta.y + 20




    # if keys_pressed[pygame.K_LEFT]:  # left
    #     globals()['current_prot_dir'] = PROT_L
    #     paolo.x -= VEL
    # if keys_pressed[pygame.K_RIGHT]: # right
    #     globals()['current_prot_dir'] = PROT_R
    #     paolo.x += VEL
    # if keys_pressed[pygame.K_UP]:  # up
    #     globals()['current_prot_dir'] = PROT_U
    #     paolo.y -= VEL
    # if keys_pressed[pygame.K_DOWN]:  # down
    #     globals()['current_prot_dir'] = PROT_D
    #     paolo.y += VEL


if __name__ == '__main__':



    clock = pygame.time.Clock()
    run = True

    paolo = pygame.Rect(WIDTH//3, HEIGHT//2, PAOLO_WIDTH, PAOLO_HEIGHT)
    casa_1 = pygame.Rect(50, 100, 200, 200)
    casa_3 = pygame.Rect(270, 50, 200, 200)
    casa_4 = pygame.Rect(500, 100, 200, 200)
    casa_big = pygame.Rect(900, 100, 250, 250)



    lista_case = []
    lista_case.append(casa_1)
    lista_case.append(casa_3)
    lista_case.append(casa_4)
    lista_case.append(casa_big)

    ingresso_porta = pygame.Rect(900 + 135 -10, 350+1, 4, 4)

    porta_interna = pygame.Rect(920 - 8, 690, 60, 40)

    while run:
        clock.tick(FPS)


        if level == 1: draw_window_level_1(paolo, casa_1, casa_3, casa_4, casa_big)
        if level == 3: draw_window_level_3(paolo, porta_interna)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed, paolo, lista_case, ingresso_porta, porta_interna)
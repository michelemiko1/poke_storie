import pygame


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


def draw_window(paolo):
    WIN.blit(GRASS, (0, 0))

    WIN.blit(current_prot_dir, (paolo.x, paolo.y))

    pygame.display.update()


def handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a]:  # left
        globals()['current_prot_dir'] = PROT_L
        yellow.x -= VEL
    if keys_pressed[pygame.K_d]: # right
        globals()['current_prot_dir'] = PROT_R
        yellow.x += VEL
    if keys_pressed[pygame.K_w]:  # up
        globals()['current_prot_dir'] = PROT_U
        yellow.y -= VEL
    if keys_pressed[pygame.K_s]:  # down
        globals()['current_prot_dir'] = PROT_D
        yellow.y += VEL


if __name__ == '__main__':



    clock = pygame.time.Clock()
    run = True

    paolo = pygame.Rect(WIDTH//3, HEIGHT//3, PAOLO_WIDTH, PAOLO_HEIGHT)

    while run:
        clock.tick(FPS)
        draw_window(paolo)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys_pressed = pygame.key.get_pressed()
        handle_movement(keys_pressed, paolo)
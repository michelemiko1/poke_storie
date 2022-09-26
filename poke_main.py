import pygame


WIDTH, HEIGHT = 1280, 720
FPS = 60

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

GRASS = pygame.image.load('images/grass.jpg')
GRASS = pygame.transform.scale(GRASS, (WIDTH, HEIGHT))

def draw_window():
    WIN.blit(GRASS, (0, 0))
    pygame.display.update()



if __name__ == '__main__':

    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)
        draw_window()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()




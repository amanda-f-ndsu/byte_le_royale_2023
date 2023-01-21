import pygame, sys

pygame.init()

size = width, height = 1366, 768
tile_size = [32, 32]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

clock = pygame.time.Clock()
simple_font = pygame.font.Font(None, 50)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()

    # DO ACTIONS
    screen.fill(black)


    # Render Frame
    pygame.display.flip()
    clock.tick(12)

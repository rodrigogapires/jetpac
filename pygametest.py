import pygame

from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()

screen = pygame.display.set_mode(
    [256, 192], pygame.FULLSCREEN | pygame.DOUBLEBUF | pygame.HWSURFACE, 32)

running = True
while running:

    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
    pygame.display.flip()

pygame.quit()

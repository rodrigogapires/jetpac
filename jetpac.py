import pygame
import sys

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
    [256, 192], pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF, 32)

background = pygame.image.load("jetpac.png")

running = True

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    screen.fill((255, 0, 0))
    screen.blit(background, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()

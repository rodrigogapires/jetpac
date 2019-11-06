import pygame
import sys
from player import Player
from rocket import Rocket
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
pygame.mouse.set_visible(0)

background = pygame.image.load("sprites\\jetpac.png").convert_alpha()

player = Player(130, 162)
rocket = Rocket()

running = True
clock = pygame.time.Clock()
while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

    player.gravity(clock.tick(30))
    keys = pygame.key.get_pressed()
    if keys[K_RIGHT]:
        player.moveRight()
    if keys[K_LEFT]:
        player.moveLeft()
    if keys[K_UP]:
        player.moveUp()
    if keys[K_DOWN]:
        player.moveDown()

    player.check()
    #print(player.x, player.y)

    rocket.getPart(player.x, player.y)

    screen.blit(player.sprite, (player.x, player.y))
    screen.blit(rocket.rocket1, (rocket.rocket1_x, rocket.rocket1_y))
    screen.blit(rocket.rocket2, (rocket.rocket2_x, rocket.rocket2_y))
    screen.blit(rocket.rocket3, (rocket.rocket3_x, rocket.rocket3_y))
    pygame.display.flip()
    clock.tick(144)

pygame.quit()
sys.exit()

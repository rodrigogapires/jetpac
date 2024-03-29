import pygame
import shelve
import sys
import random

from player import Player
from rocket import Rocket
from fuel import Fuel
from bullet import RightBullet, LeftBullet
from class_enemy import EnemyRight, EnemyLeft
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_e,
    K_h,
    K_ESCAPE,
    K_RETURN,
    KEYDOWN,
)


def text(text, color, x, y):
    text = font.render(text, False, color, None)
    rect = text.get_rect()
    rect = (x, y)
    screen.blit(text, rect)


def addEnemyCondition(enemies, sprites, enemy_limit):
    if len(enemies) < enemy_limit:
        aleatorio = random.randint(0, 1)
        if aleatorio == 0:
            new_enemy = EnemyLeft(-16, random.randint(0, 162))
            enemies.add(new_enemy)
            sprites.add(new_enemy)
        else:
            new_enemy = EnemyRight(256, random.randint(0, 162))
            enemies.add(new_enemy)
            sprites.add(new_enemy)


screen_width = 256
screen_height = 192
flags = pygame.SCALED | pygame.FULLSCREEN

pygame.mixer.pre_init(48000, -16, 1, 512)
pygame.init()

screen = pygame.display.set_mode([screen_width, screen_height], flags, vsync=1)

pygame.mouse.set_visible(0)

font = pygame.font.Font("jetpac.ttf", 6)
background = pygame.image.load("sprites\\jetpac.png").convert_alpha()
lifes = pygame.image.load("sprites\\lifes.png").convert_alpha()

lastScore = 0
running = True
intro = True
game = True

while running:

    player = Player(130, 162)
    rocket = Rocket()
    fuel = Fuel()

    enemy_limit = 8
    ADDENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDENEMY, 250)

    aliens = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    all_sprites = pygame.sprite.Group()

    # RIGHT = 0 //// LEFT = 1
    right_left = 0

    fps = 0
    clock = pygame.time.Clock()

    while intro:
        game = True
        HARD_MODE = False

        screen.fill((0, 0, 0))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    intro = False
                    game = False
                    running = False
                if event.key == K_RETURN:
                    intro = False
                if event.key == K_h:
                    HARD_MODE = True
                    intro = False

        text("hi", (0, 255, 255), 121, 1)
        text(str(player.hiscore).zfill(6), (255, 255, 0), 105, 9)
        text("1up", (255, 255, 255), 25, 1)
        text(str(lastScore).zfill(6), (255, 255, 0), 9, 9)
        text("jetpac game selection", (255, 255, 255), 49, 33)
        text("enter 1 player game", (255, 255, 255), 49, 57)
        text("  h   hardcore game", (255, 255, 255), 49, 73)
        text(" esc  quit", (255, 255, 255), 49, 89)

        pygame.display.flip()
        clock.tick(31)
        fps = clock.get_fps()

    while game:
        pause = False

        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    game = False
                    intro = True
                if event.key == K_RETURN:
                    pause = True
                if event.key == K_SPACE:
                    if right_left == 0:
                        bullet = RightBullet(player.x, player.y)
                        bullets.add(bullet)
                        all_sprites.add(bullet)
                    else:
                        bullet = LeftBullet(player.x, player.y)
                        bullets.add(bullet)
                        all_sprites.add(bullet)
            elif event.type == ADDENEMY:
                addEnemyCondition(aliens, all_sprites, enemy_limit)

        while pause == True:
            for event in pygame.event.get():
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        pause = False

        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            player.moveRight()
            right_left = 0
        if keys[K_LEFT]:
            player.moveLeft()
            right_left = 1
        if keys[K_UP]:
            player.moveUp()
        if keys[K_DOWN]:
            player.moveDown()

        a = 0
        hit_player = False

        player.gravity()

        aliens.update(HARD_MODE)

        for i in aliens:
            if player.hit(i.x, i.y) is True:
                player.x = 130
                player.y = 162
                for enemy in aliens:
                    enemy.kill()
            bullets.update(a, i, i.x, i.y, player)
            a += 1

        if rocket.stage < 3:
            rocket.collision()
            rocket.get(player.x, player.y, player)

        if rocket.stage == 3 and fuel.used < 6:
            fuel.gravity()
            fuel.collision()
            fuel.get(player.x, player.y, player)
            screen.blit(fuel.sprite, (fuel.x, fuel.y))

        player.collision()
        rocket.getIn(fuel.used, player.x, player.y)

        if rocket.inside is False:
            screen.blit(player.sprite, (player.x, player.y))
        elif rocket.inside is True and rocket.stage == 4 and rocket.rocket1_y == 168:
            fuel.used = 0
            rocket.inside = False
            rocket.stage = 3
            rocket.i = 0
            player.x = 130
            player.y = 162
            enemy_limit += 3
        else:
            rocket.nextLevel()
            for enemy in aliens:
                enemy.kill()

        if player.lifes < 0:
            lastScore = player.score
            if player.score > shelve.open("hiscore")["hiscore"]:
                shelve.open("hiscore")["hiscore"] = player.score
            shelve.open("hiscore").close()
            game = False
            intro = True

        lifes_text = font.render(str(player.lifes), False, (255, 255, 255), None)
        lifesRect = lifes_text.get_rect()
        lifesRect = (66, 1)

        rocket.fuel(fuel.used)
        screen.blit(rocket.rocket1, (rocket.rocket1_x, rocket.rocket1_y))
        screen.blit(rocket.rocket2, (rocket.rocket2_x, rocket.rocket2_y))
        screen.blit(rocket.rocket3, (rocket.rocket3_x, rocket.rocket3_y))
        for i in all_sprites:
            screen.blit(i.sprite, (i.x, i.y))
        if player.lifes > 0:
            screen.blit(lifes_text, lifesRect)
            screen.blit(lifes, (73, 0))

        text("hi", (0, 255, 255), 121, 1)
        text(str(player.hiscore).zfill(6), (255, 255, 0), 105, 9)
        text("1up", (255, 255, 255), 25, 1)
        text(str(player.score).zfill(6), (255, 255, 0), 9, 9)
        text(str(int(fps)), (0, 255, 0), 242, 1)

        pygame.display.flip()
        clock.tick(31)
        fps = clock.get_fps()

pygame.quit()
sys.exit()

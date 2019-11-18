import pygame
import sys
import random
from player import Player
from rocket import Rocket
from fuel import Fuel
from bullet import RightBullet, LeftBullet
from class_enemy import Enemy, EnemyRight
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
    K_ESCAPE,
    KEYDOWN,
)




pygame.init()
screen = pygame.display.set_mode(
    [256, 192], pygame.FULLSCREEN | pygame.HWSURFACE | pygame.DOUBLEBUF, 32)
pygame.mouse.set_visible(0)

background = pygame.image.load("sprites\\jetpac.png").convert_alpha()

player = Player(130, 162)
rocket = Rocket()
fuel = Fuel()






ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)


aliens = pygame.sprite.Group()
bullets = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()

# RIGHT = 0 //// LEFT = 1
right_left = 0

running = True
clock = pygame.time.Clock()

while running:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False
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
            if len(aliens) < 8:
                aleatorio = random.randint(0, 1)
                if aleatorio == 0:
                    new_enemy = Enemy(-80, random.randint(0, 162))
                    aliens.add(new_enemy)
                    all_sprites.add(new_enemy)
                    
                else:
                    new_enemy = EnemyRight(242+80, random.randint(0, 162))
                    aliens.add(new_enemy)
                    all_sprites.add(new_enemy)   
                    

    font = pygame.font.SysFont('Consolas',15)
    text =font.render (str(player.lifes),False,(255,255,255),None)
    textRect = text.get_rect() 
    textRect.center = (256 // 2, 8) 


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
        
    a=0    
    hit_player = False
    
    
    player.gravity()
    player.collision()
    aliens.update()
    
    
    for i in aliens:
        if player.hit(i.x,i.y) is True:
            player.x = 130
            player.y = 162
            for enemy in aliens:            
                enemy.kill()
        bullets.update(a,i, i.x, i.y)
        a+=1
        


    if rocket.stage < 3:
        rocket.get(player.x, player.y)

    if rocket.stage == 3 and fuel.used < 6:
        fuel.gravity()
        fuel.collision()
        fuel.get(player.x, player.y)
        screen.blit(fuel.sprite, (fuel.x, fuel.y))

    rocket.getIn(fuel.used, player.x, player.y)
    if rocket.inside is False:
        screen.blit(player.sprite, (player.x, player.y))
    elif rocket.inside is True and rocket.stage == 4 and rocket.rocket1_y == 168:
        fuel.used = 0
        rocket.inside = False
        rocket.stage = 3
        player.x = 130
        player.y = 162
    else:
        rocket.nextLevel()
        for enemy in aliens:
                enemy.kill()
    
       
        
    if player.lifes < 1:
        running = False
    
    for i in all_sprites:
        screen.blit(i.sprite, (i.x, i.y))
    rocket.fuel(fuel.used)
    screen.blit(rocket.rocket1, (rocket.rocket1_x, rocket.rocket1_y))
    screen.blit(rocket.rocket2, (rocket.rocket2_x, rocket.rocket2_y))
    screen.blit(rocket.rocket3, (rocket.rocket3_x, rocket.rocket3_y))
    screen.blit(text, textRect)
    pygame.display.flip()
    clock.tick(30)
    
    
pygame.quit()
sys.exit()

import pygame
import random 

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\enemy2.png").convert_alpha()
        self.x = x
        self.y = y
        self.speed = random.randint(1, 2)
        self.hard_speed = random.randint(2, 4)
        
    def update(self, hard):
        if hard == True:
            self.x += self.hard_speed
        else:
            self.x += self.speed
            
        if self.x > 242:
            self.kill()
            
class EnemyRight(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\enemy.png").convert_alpha()
        self.x = x
        self.y = y
        self.speed = random.randint(1, 2)
        self.hard_speed = random.randint(2, 4)
 
    def update(self, hard):
        if hard == True:
            self.x -= self.hard_speed
        else:
            self.x -= self.speed
            
        if self.x < 0:
            self.kill()

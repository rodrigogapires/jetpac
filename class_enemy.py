import pygame
import random 

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y, enemy_sprite):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load(enemy_sprite).convert_alpha()
        self.x = x
        self.y = y
        self.speed = random.randint(1, 2)
        self.hard_speed = random.randint(2, 4)
        
    def update(self, hard, screen_limit):
        if hard == True:
            self.x += self.hard_speed
        else:
            self.x += self.speed

        if screen_limit == 0:    
            if self.x < screen_limit:
                self.kill()
        else:
            if self.x > screen_limit:
                self.kill()

class EnemyLeft(Enemy):
    def __init__(self,x,y):
        super().__init__(x, y, "sprites\\enemy2.png")
        
    def update(self, hard):
        super().update(hard, 242)
            
class EnemyRight(Enemy):
    def __init__(self,x,y):
        super().__init__(x, y, "sprites\\enemy.png")
        self.hard_speed = -self.hard_speed
        self.speed = -self.speed
 
    def update(self, hard):
        super().update(hard, 0)

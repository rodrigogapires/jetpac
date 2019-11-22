import pygame

class RightBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\fuel.png").convert_alpha()
        self.x = x
        self.y = y
        
    def update(self,a,enemy, enemy_x, enemy_y):     
        if a == 0:
            self.x += 3
        
        elif abs(self.x - enemy_x) < 17 and abs(self.y - enemy_y) <10:
            self.kill()
            enemy.kill()
     
        
class LeftBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\fuel.png").convert_alpha()
        self.x = x
        self.y = y
        
    def update(self,a,enemy, enemy_x, enemy_y):     
        if a == 0:
            self.x -= 3
              
        elif abs(self.x - enemy_x) < 17 and abs(self.y - enemy_y) <10:
            self.kill()
            enemy.kill()
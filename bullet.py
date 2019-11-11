import pygame

class RightBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\fuel.png").convert_alpha()
        self.x = x
        self.y = y
        
    def update(self):       
        self.x += 3
        
class LeftBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\fuel.png").convert_alpha()
        self.x = x
        self.y = y
        
    def update(self):       
        self.x -= 3

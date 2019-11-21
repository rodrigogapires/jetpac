import pygame

class RightBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\fuel.png").convert_alpha()
        self.x = x
        self.y = y

    def update(self,a,enemy, enemy_x, enemy_y, player):     
        if a == 0:
            self.x += 5

        elif self.x - enemy_x < 16 and self.x - enemy_x > 0 and self.y - enemy_y < 11 and self.y - enemy_y > 0:
            self.kill()
            enemy.kill()
            player.score += 25

class LeftBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\fuel.png").convert_alpha()
        self.x = x
        self.y = y

    def update(self,a,enemy, enemy_x, enemy_y, player):     
        if a == 0:
            self.x -= 5

        elif self.x - enemy_x < 16 and self.x - enemy_x > 0 and self.y - enemy_y < 11 and self.y - enemy_y > 0:
            self.kill()
            enemy.kill()
            player.score += 25

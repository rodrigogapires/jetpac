import pygame


class RightBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\bullet_right.png").convert_alpha()
        self.killSound = pygame.mixer.Sound('sound\\kill.wav')
        self.x = x 
        self.y = y + 3
        self.life = 0

        pygame.mixer.Sound('sound\\fire.wav').play()

    def update(self, a, enemy, enemy_x, enemy_y, player):
        self.life += 1
        
        if self.life == 200:
            self.kill()

        if a == 0:
            self.x += 5
            if abs(self.x - enemy_x) < 17 and abs(self.y - enemy_y) <10:
                self.kill()
                enemy.kill()
                self.killSound.play()
                player.score += 25
            elif self.x > 242:
                self.x = 0
            elif self.x < 0:
                self.x = 242

        elif abs(self.x - enemy_x) < 17 and abs(self.y - enemy_y) <10:
            self.kill()
            enemy.kill()
            self.killSound.play()
            player.score += 25

class LeftBullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprite = pygame.image.load("sprites\\bullet_left.png").convert_alpha()
        self.killSound = pygame.mixer.Sound('sound\\kill.wav')
        self.x = x
        self.y = y + 3
        self.life = 0

        pygame.mixer.Sound('sound\\fire.wav').play()

    def update(self, a, enemy, enemy_x, enemy_y, player):
        self.life += 1

        if self.life == 200:
            self.kill()

        elif a == 0:
            self.x -= 5
            if abs(self.x - enemy_x) < 17 and abs(self.y - enemy_y) <10:
                self.kill()
                enemy.kill()
                self.killSound.play()
                player.score += 25
            elif self.x > 242:
                self.x = 0
            elif self.x < 0:
                self.x = 242

        elif abs(self.x - enemy_x) < 17 and abs(self.y - enemy_y) <10:
            self.kill()
            enemy.kill()
            self.killSound.play()
            player.score += 25

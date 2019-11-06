import pygame


class Player:
    def __init__(self, x, y):
        self.sprite = pygame.image.load("sprites\\player.png").convert_alpha()
        self.lifes = 3
        self.x = x
        self.y = y

    def gun(self):
        pass

    def gravity(self):
        self.y += 2

    def moveRight(self):
        self.sprite = pygame.image.load("sprites\\player.png").convert_alpha()
        self.x += 2

    def moveLeft(self):
        self.sprite = pygame.image.load("sprites\\player2.png").convert_alpha()
        self.x -= 2

    def moveUp(self):
        self.y -= 5

    def moveDown(self):
        self.y += 1

    def collision(self):

        # Bordas
        if self.x > 242:
            self.x = 242

        if self.x < 0:
            self.x = 0

        if self.y > 162:
            self.y = 162

        if self.y < 0:
            self.y = 0

        # Plataforma esquerda
        if self.y > 50 and self.y < 55 and self.x > 22 and self.x < 74:
            self.y = 50

        if self.y > 55 and self.y < 80 and self.x > 22 and self.x < 74:
            self.y = 80

        # Plataforma direita
        if self.y > 26 and self.y < 31 and self.x > 182 and self.x < 235:
            self.y = 26

        if self.y > 31 and self.y < 56 and self.x > 182 and self.x < 235:
            self.y = 56

        # Plataforma centro
        if self.y > 74 and self.y < 80 and self.x > 110 and self.x < 150:
            self.y = 74

        if self.y > 80 and self.y < 104 and self.x > 110 and self.x < 150:
            self.y = 104

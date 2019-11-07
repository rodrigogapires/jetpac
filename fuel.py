import pygame
import random


class Fuel:
    def __init__(self):
        self.sprite = pygame.image.load("sprites\\fuel.png").convert_alpha()
        self.used = 0
        self.x = random.randrange(0, 240, 10)
        self.y = -16

    def gravity(self):
        self.y += 1

    def getFuel(self, player_x, player_y):
        if self.x == 168 and self.y < 171:
            if self.y == 170:
                self.used += 1
                self.x = random.randrange(0, 240, 20)
                self.y = -16

        elif abs(player_x - self.x) < 5 and abs(player_y - self.y) < 10:
            self.x = player_x
            self.y = player_y

    def collision(self):

        # Bordas
        if self.y > 171:
            self.y = 171

        # Plataforma esquerda
        if self.y > 59 and self.y < 89 and self.x > 22 and self.x < 74:
            self.y = 59

        # Plataforma direita
        if self.y > 35 and self.y < 65 and self.x > 182 and self.x < 235:
            self.y = 35

        # Plataforma centro
        if self.y > 83 and self.y < 113 and self.x > 110 and self.x < 150:
            self.y = 83

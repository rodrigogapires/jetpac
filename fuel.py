import pygame
import random


class Fuel:
    def __init__(self):
        self.sprite = pygame.image.load("sprites\\fuel.png").convert_alpha()
        self.getSound = pygame.mixer.Sound('sound\\get.wav')
        self.fuelSound = pygame.mixer.Sound('sound\\fuel.wav')
        self.used = 0
        self.spawns = [8, 32, 40, 48, 56, 64, 88, 96, 136, 192, 224]
        self.x = random.choice(self.spawns)
        self.y = -16
        self.i = 0

    def gravity(self):
        self.y += 1

    def get(self, player_x, player_y, player):
        if self.x == 168 and self.y < 171:
            if self.y == 170:
                self.fuelSound.play()
                self.used += 1
                self.x = random.choice(self.spawns)
                self.y = -16
                self.i = 0
                player.score += 100

        elif abs(player_x - self.x) < 5 and abs(player_y - self.y) < 10:
            if self.i == 0:
                self.getSound.play()
                player.score += 100
                self.i = 1
            self.x = player_x
            self.y = player_y

    def collision(self):
        # Bordas
        if self.x > 242:
            self.x = 0

        if self.x < 0:
            self.x = 242

        if self.y > 171:
            self.y = 171

        # Plataforma esquerda
        if self.y > 59 and self.y < 64 and self.x > 22 and self.x < 74:
            self.y = 59

        # Plataforma direita
        if self.y > 35 and self.y < 40 and self.x > 182 and self.x < 235:
            self.y = 35

        # Plataforma centro
        if self.y > 83 and self.y < 88 and self.x > 110 and self.x < 150:
            self.y = 83

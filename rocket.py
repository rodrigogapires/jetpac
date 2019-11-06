import pygame


class Rocket:
    def __init__(self):
        self.rocket1 = pygame.image.load(
            "sprites\\rocket1.png").convert_alpha()
        self.rocket2 = pygame.image.load(
            "sprites\\rocket2.png").convert_alpha()
        self.rocket3 = pygame.image.load(
            "sprites\\rocket3.png").convert_alpha()
        self.rocket1_x = 168
        self.rocket1_y = 168
        self.rocket2_x = 128
        self.rocket2_y = 80
        self.rocket3_x = 48
        self.rocket3_y = 56

    def getPart(self, player_x, player_y):
        if self.rocket2_x == player_x and self.rocket2_y == player_y + 5:
            print("pegou 2")
            self.rocket2_x = player_x
            self.rocket2_y = player_y

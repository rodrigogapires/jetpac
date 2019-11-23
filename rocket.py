import pygame


class Rocket:
    def __init__(self):
        self.rocket1 = pygame.image.load("sprites\\rocket1.png").convert_alpha()
        self.rocket2 = pygame.image.load("sprites\\rocket2.png").convert_alpha()
        self.rocket3 = pygame.image.load("sprites\\rocket3.png").convert_alpha()
        self.stage = 1
        self.inside = False
        self.rocket1_x = 168
        self.rocket1_y = 168
        self.rocket2_x = 128
        self.rocket2_y = 80
        self.rocket3_x = 48
        self.rocket3_y = 56

    def get(self, player_x, player_y, player):
        if self.stage == 1 and self.rocket2_x == 168 and self.rocket2_y < 152:
            self.rocket2_y += 1
            if self.rocket2_y == 152:
                self.stage = 2
                player.score += 100

        elif self.stage == 1 and abs(player_x - self.rocket2_x) < 5 and abs(player_y - self.rocket2_y) < 8:
            self.rocket2_x = player_x
            self.rocket2_y = player_y

        if self.stage == 2 and self.rocket3_x == 168 and self.rocket3_y < 136:
            self.rocket3_y += 1
            if self.rocket3_y == 136:
                self.stage = 3
                player.score += 100

        elif self.stage == 2 and abs(player_x - self.rocket3_x) < 5 and abs(player_y - self.rocket3_y) < 8:
            self.rocket3_x = player_x
            self.rocket3_y = player_y

    def fuel(self, fuel):
        if fuel == 0:
            self.rocket1 = pygame.image.load("sprites\\rocket1.png").convert_alpha()
            self.rocket2 = pygame.image.load("sprites\\rocket2.png").convert_alpha()
            self.rocket3 = pygame.image.load("sprites\\rocket3.png").convert_alpha()
        elif fuel == 1:
            self.rocket1 = pygame.image.load("sprites\\rocket1_fuel1.png").convert_alpha()
            self.rocket2 = pygame.image.load("sprites\\rocket2.png").convert_alpha()
            self.rocket3 = pygame.image.load("sprites\\rocket3.png").convert_alpha()
        elif fuel == 2:
            self.rocket1 = pygame.image.load("sprites\\rocket1_fuel2.png").convert_alpha()
            self.rocket2 = pygame.image.load("sprites\\rocket2.png").convert_alpha()
            self.rocket3 = pygame.image.load("sprites\\rocket3.png").convert_alpha()
        elif fuel == 3:
            self.rocket1 = pygame.image.load("sprites\\rocket1_fuel2.png").convert_alpha()
            self.rocket2 = pygame.image.load("sprites\\rocket2_fuel1.png").convert_alpha()
            self.rocket3 = pygame.image.load("sprites\\rocket3.png").convert_alpha()
        elif fuel == 4:
            self.rocket1 = pygame.image.load("sprites\\rocket1_fuel2.png").convert_alpha()
            self.rocket2 = pygame.image.load("sprites\\rocket2_fuel2.png").convert_alpha()
            self.rocket3 = pygame.image.load("sprites\\rocket3.png").convert_alpha()
        elif fuel == 5:
            self.rocket1 = pygame.image.load("sprites\\rocket1_fuel2.png").convert_alpha()
            self.rocket2 = pygame.image.load("sprites\\rocket2_fuel2.png").convert_alpha()
            self.rocket3 = pygame.image.load("sprites\\rocket3_fuel1.png").convert_alpha()
        elif fuel == 6:
            self.rocket1 = pygame.image.load("sprites\\rocket1_fuel2.png").convert_alpha()
            self.rocket2 = pygame.image.load("sprites\\rocket2_fuel2.png").convert_alpha()
            self.rocket3 = pygame.image.load("sprites\\rocket3_fuel2.png").convert_alpha()

    def getIn(self, fuel, player_x, player_y):
        if fuel == 6 and abs(player_x - self.rocket1_x) < 5 and abs(player_y - self.rocket1_y) < 8:
            self.inside = True

    def nextLevel(self):
        if self.rocket1_y > -16 and self.stage == 3:
            self.rocket1_y -= 1
            self.rocket2_y -= 1
            self.rocket3_y -= 1
        elif self.rocket1_y == -16 and self.stage == 3:
            self.stage = 4
        elif self.rocket1_y < 168 and self.stage == 4:
            self.rocket1_y += 1
            self.rocket2_y += 1
            self.rocket3_y += 1

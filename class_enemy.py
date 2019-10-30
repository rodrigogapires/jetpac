class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.image = pygame.image.load('apple.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect(
             center=(
                 random.randint(1920 + 20, 1920 + 100),
                 random.randint(0, 1080),
             )
         )
        self.speed = random.randint(5, 10)
        
    
import pygame
from pygame.sprite import Sprite
import random


class Star(Sprite):
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        self.stars_type = []
        self.image = pygame.image.load('images/stars.png')
        for i in range(3):
            self.stars_type.append(pygame.transform.smoothscale(self.image.subsurface(pygame.Rect(27 * i , 0, 27, 25)), (20, 20)))

        self.image = self.stars_type[random.randint(0,2)]
        dx = random.randint(1,20)
        self.image = pygame.transform.smoothscale(self.image, (dx, dx))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

    def update(self):
        self.y += self.settings.star_speed
        self.rect.y = self.y


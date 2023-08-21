import pygame
import magic2d.resouces
from magic2d.util import ImageHandleTools

class PlayerHealth(pygame.sprite.Sprite):

    type = 'playerhealth'
    curr = 0


    def __init__(self, x, y):
        super().__init__()
        self.image = ImageHandleTools.widthScale(magic2d.resouces.playerHealth, 200)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.width = self.rect.width
        self.height = self.rect.height

        # self.progress = pygame.Surface((self.rect.width, self.rect.height))
        # self.progress.

    def setHealth(self, health):
        self.curr = health

    def update(self):
        self.image = ImageHandleTools.widthScale(magic2d.resouces.playerHealth, 200)
        health = self.curr / 100 * 191
        pygame.draw.rect(self.image, [231, 76, 60, 200], [4, 5, health, 15], 0)
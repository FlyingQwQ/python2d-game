import pygame
import magic2d.resouces
from magic2d.util import ImageHandleTools

class ArmsHouse(pygame.sprite.Sprite):

    def __init__(self, x, y):
        super().__init__()
        self.image = ImageHandleTools.widthScale(magic2d.resouces.armshouse, 120)
        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
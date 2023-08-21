import pygame
import magic2d.resouces
import magic2d.world.block.basicblock
from magic2d.util import ImageHandleTools


class Leavesoak(pygame.sprite.Sprite, magic2d.world.block.basicblock.BasicBlock):

    blockId = 11
    collision = False

    def __init__(self):
        super().__init__()
        self.imgfile = ImageHandleTools.scale(magic2d.resouces.leaves_oak, 30, 30)
        self.image = pygame.Surface((30, 30))
        self.image.set_colorkey((0, 0, 0))
        self.image.blit(self.imgfile, (0, 0))
        self.rect = self.image.get_rect()

        self.hardness = 3
        self.grayscale = False

    def update(self):
        self.destroyAnima()
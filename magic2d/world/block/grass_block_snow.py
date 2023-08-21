import pygame
import magic2d.resouces
import magic2d.world.block.basicblock
from magic2d.util import ImageHandleTools

class GrassBlockSnow(pygame.sprite.Sprite, magic2d.world.block.basicblock.BasicBlock):

    blockId = 7
    collision = True

    def __init__(self):
        super().__init__()
        self.imgfile = ImageHandleTools.scale(magic2d.resouces.grass_block_snow, 30, 30)
        self.image = pygame.Surface((30, 30))
        self.image.blit(self.imgfile, (0, 0))
        self.rect = self.image.get_rect()

        self.hardness = 5
        self.itemType = 'soilblockitem.SoilBlockItem'

    def update(self):
        self.destroyAnima()
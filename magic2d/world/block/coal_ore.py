import pygame
import magic2d.resouces
import magic2d.world.block.basicblock
from magic2d.util import ImageHandleTools


class CoalOre(pygame.sprite.Sprite, magic2d.world.block.basicblock.BasicBlock):

    blockId = 8
    collision = True

    def __init__(self):
        super().__init__()
        self.imgfile = ImageHandleTools.scale(magic2d.resouces.coal_ore, 30, 30)
        self.image = pygame.Surface((30, 30))
        self.image.blit(self.imgfile, (0, 0))
        self.rect = self.image.get_rect()

        self.hardness = 30
        self.itemType = 'coalitem.CoalItem'

    def update(self):
        self.destroyAnima()
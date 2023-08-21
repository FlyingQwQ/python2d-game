import pygame
import magic2d.world.block.basicblock


class Air(pygame.sprite.Sprite, magic2d.world.block.basicblock.BasicBlock):

    blockId = 0
    collision = False   #是否可以碰撞

    def __init__(self):
        super().__init__()
        self.imgfile = None
        self.image = pygame.Surface((30, 30))
        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        self.hardness = -1

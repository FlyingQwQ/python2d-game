import pygame
import magic2d.resouces
import magic2d.item.basicitem
from magic2d.util import ImageHandleTools

class WoodPickaxe(magic2d.item.basicitem.BasicItem):

    #工具的挖掘等级
    excavationLevel = 10

    def __init__(self):
        self.image = ImageHandleTools.widthScale(magic2d.resouces.woodpickaxe, 42)

        self.itemType = 'tool'
        self.itemClass = 'wood_pickaxe.WoodPickaxe'
        self.stackable = False
        self.selectIndicatorVisible = True
        self.range = 10

        self.handImage = magic2d.resouces.woodpickaxe
        self.handImage = pygame.transform.rotate(self.handImage, 90)
        self.handImageWidth = 25
        self.handImageHeight = 25

    def useItem(self, worldObj):
        blockX, blockY = worldObj.getMousePos()
        block = worldObj.getBlock(blockX, blockY)
        block.startExcavate()
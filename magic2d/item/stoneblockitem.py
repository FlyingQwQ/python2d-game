import pygame
import magic2d.resouces
import magic2d.item.basicitem
from magic2d.util import ImageHandleTools

class StoneBlockItem(magic2d.item.basicitem.BasicItem):

    def __init__(self):
        self.image = ImageHandleTools.widthScale(magic2d.resouces.stone, 42)

        self.itemType = 'block'
        self.itemClass = 'stoneblockitem.StoneBlockItem'
        self.blockType = 'stone.Stone'
        self.selectIndicatorVisible = True

        self.handImage = self.image
        self.handImageWidth = 10
        self.handImageHeight = 10
import pygame
import magic2d.resouces
import magic2d.item.basicitem
from magic2d.util import ImageHandleTools

class GrassBlockItem(magic2d.item.basicitem.BasicItem):

    def __init__(self):
        self.image = ImageHandleTools.widthScale(magic2d.resouces.grass, 42)

        self.itemType = 'block'
        self.itemClass = 'grassblockitem.GrassBlockItem'
        self.blockType = 'grass.Grass'
        self.selectIndicatorVisible = True

        self.handImage = self.image
        self.handImageWidth = 10
        self.handImageHeight = 10
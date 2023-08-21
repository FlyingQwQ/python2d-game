import pygame
import magic2d.resouces
import magic2d.item.basicitem
from magic2d.util import ImageHandleTools

class CoalItem(magic2d.item.basicitem.BasicItem):

    def __init__(self):
        self.image = ImageHandleTools.widthScale(magic2d.resouces.coalitem, 42)

        self.itemType = 'block'
        self.itemClass = 'coalitem.CoalItem'
        self.selectIndicatorVisible = True

        self.handImage = self.image
        self.handImageWidth = 14
        self.handImageHeight = 14
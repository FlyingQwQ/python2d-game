import pygame
import math
import magic2d.resouces
import magic2d.item.basicitem
from magic2d.magic import *
from magic2d.util import ImageHandleTools

class CycloneStaffItem(magic2d.item.basicitem.BasicItem):

    def __init__(self):
        self.image = ImageHandleTools.widthScale(magic2d.resouces.cyclonestaff, 49)
        self.image = pygame.transform.rotate(self.image, -40)

        self.itemType = 'tool'
        self.itemClass = 'cyclonestaffitem.CycloneStaffItem'
        self.stackable = False
        self.range = 15

        self.handImage = self.image
        self.handImage = pygame.transform.rotate(self.handImage, 0)
        self.handImageWidth = 40
        self.handImageHeight = 35



    def useItem(self, worldObj):
        mouseX = pygame.mouse.get_pos()[0] + worldObj.cameraRect.x

        blockX, blockY = worldObj.getMousePos()
        block = worldObj.getBlock(blockX, blockY)
        if not block.collision:
            footBlock = worldObj.getBlock(blockX, blockY + 1)
            if footBlock.collision:
                player = worldObj.getPlayer()
                cycloneMagic = magic1.CycloneMagic()
                cycloneMagic.setSpeed(0)
                worldObj.sendMagic(cycloneMagic, player.rect.x, player.rect.y, mouseX - (cycloneMagic.rect.width / 2), (footBlock.rect.y - cycloneMagic.rect.height) + 10)
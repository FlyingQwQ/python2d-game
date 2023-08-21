import pygame
import magic2d.resouces
import magic2d.item.basicitem
from magic2d.magic import *
from magic2d.util import ImageHandleTools

class Arms1Item(magic2d.item.basicitem.BasicItem):

    def __init__(self):
        self.image = magic2d.resouces.arms1
        self.image = pygame.transform.rotate(self.image, -40)

        self.itemType = 'tool'
        self.itemClass = 'arms1item.Arms1Item'
        self.stackable = False
        self.range = 10

        self.handImage = magic2d.resouces.arms1
        self.handImage = pygame.transform.rotate(self.handImage, -30)
        self.handImageWidth = 30
        self.handImageHeight = 30

    def useItem(self, worldObj):
        mouseX = pygame.mouse.get_pos()[0] + worldObj.cameraRect.x
        mouseY = pygame.mouse.get_pos()[1] + worldObj.cameraRect.y

        player = worldObj.getPlayer()
        electricBallMagic = magic2.ElectricBallMagic()
        electricBallMagic.setSpeed(5)
        worldObj.sendMagic(electricBallMagic, player.rect.x, player.rect.y, mouseX - electricBallMagic.width / 2, mouseY - electricBallMagic.height / 2)
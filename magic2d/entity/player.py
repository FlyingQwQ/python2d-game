import pygame
import magic2d.resouces
import magic2d.entity.entitylive
from magic2d.ui import ui
from magic2d.util import ImageHandleTools
from magic2d.entity.enum.directionstate import DirectionState
from magic2d.entity.enum.movestate import MoveState
from magic2d.ui.healthdecoration import playerhealth


class Player(pygame.sprite.Sprite, magic2d.entity.entitylive.EntityLive):

    entityType = 'player'
    health = 100


    def __init__(self, x, y):
        super().__init__()
        self.image = magic2d.resouces.playerRightFrame[0]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.maxSpeed = 5

        # 每帧的延迟，已秒为单位
        self.frameAnimationsDelay = 0.1
        # 帧数
        self.frameAnimationsNumber = 2
        # 帧动画左边
        self.frameAnimationsLeft = magic2d.resouces.playerLeftFrame
        # 帧动画右边
        self.frameAnimationsRight = magic2d.resouces.playerRightFrame

        self.playerHealth = playerhealth.PlayerHealth(10, 10)
        ui.UIGroup.add(self.playerHealth)

    def setItemBox(self, itemBoxObj):
        self.itemBoxObj = itemBoxObj

    def getItemBox(self):
        return self.itemBoxObj

    def setHandItem(self, handItemObj):
        self.handItemObj = handItemObj

    def update(self):
        self.handItemObj.setLocation(self.rect.x - self.worldObj.cameraRect.x, self.rect.y - self.worldObj.cameraRect.y)

        self.actionUpdate()
        self.modelUpdate()

        self.playerHealth.setHealth(self.health)
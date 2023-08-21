import pygame
import time
import magic2d.resouces
import magic2d.entity.enum.movestate
from magic2d.util import ImageHandleTools
from magic2d.entity.enum.movestate import MoveState

class HandItem(pygame.sprite.Sprite):

    isUse = False
    visible = False

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

    def setLocation(self, x, y):
        player = self.worldObj.getPlayer()
        self.item = self.itemBoxObj.getCurrItem()
        handImageWidth = 0
        handImageHeight = 0
        if self.item != 0:
            handImageWidth = self.item.handImageWidth
            handImageHeight = self.item.handImageHeight

        if player.moveState == MoveState.RIGHT or player.moveState == MoveState.RIGHTWALK:
            self.rect.x = ((x + player.rect.width) - (player.rect.width / 2) - (handImageWidth / 2)) + 10
        if player.moveState == MoveState.LEFT or player.moveState == MoveState.LEFTWALK:
            self.rect.x = ((x + player.rect.width) - (player.rect.width / 2) - (handImageWidth / 2)) - 10
        self.rect.y = (y + player.rect.height) - (player.rect.height / 2) - (handImageHeight / 2) + 5

    def setWorld(self, worldObj):
        self.worldObj = worldObj

    def setItemBox(self, itemBoxObj):
        self.itemBoxObj = itemBoxObj

    def setVisible(self, visible):
        self.visible = visible
        if not visible:
            self.image = pygame.Surface((10, 10))
            self.image.set_colorkey((0, 0, 0))
        else:
            self.moveAnimaTime = time.time()

    def update(self):
        if self.visible:
            if self.item != 0:
                player = self.worldObj.getPlayer()
                self.image = ImageHandleTools.scale(self.item.handImage, self.item.handImageWidth, self.item.handImageHeight)
                if player.moveState == MoveState.RIGHT or player.moveState == MoveState.RIGHTWALK:
                    self.image = pygame.transform.flip(self.image, True, False)

            currTime = time.time()
            if currTime - self.moveAnimaTime > 0.2:
                self.image = pygame.Surface((10, 10))
                self.image.set_colorkey((0, 0, 0))
                self.visible = False
                self.moveAnimaTime = currTime
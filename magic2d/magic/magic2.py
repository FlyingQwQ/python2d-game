import pygame
import time
import magic2d.resouces
from magic2d.util import Math

class ElectricBallMagic(pygame.sprite.Sprite):

    endX = 0
    endY = 0
    speed = 0
    # 完成销毁魔法
    complete = False

    width = 30
    height = 30

    # 攻击力
    hurt = 7

    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale(magic2d.resouces.magic2Frame[0], (self.width, self.height))
        self.rect = self.image.get_rect()

    frameIndex = 1
    moveAnimaTime = 0
    def animation(self):
        currTime = time.time()
        if currTime - self.moveAnimaTime > 0.1:
            self.frameIndex += 1
            if self.frameIndex > 6:
                self.frameIndex = 1
            self.image = pygame.transform.scale(magic2d.resouces.magic2Frame[self.frameIndex - 1], (self.width, self.height))
            self.moveAnimaTime = currTime

    '''
        设置攻击的开始位置和结束位置
    '''
    def setRoute(self, startX, startY, endX, endY):
        self.rect.x = startX
        self.rect.y = startY
        self.endX = endX
        self.endY = endY

    def setWorld(self, worldObj):
        self.worldObj = worldObj

    def setSpeed(self, speed):
        self.speed = speed

    '''
        碰到生物事件
    '''
    def entityCollision(self):
        for entity in pygame.sprite.spritecollide(self, self.worldObj.entityGroup, False):
            if entity.entityType != 'player':
                self.complete = True
                entity.deductHealth(self.hurt)
                break


    def update(self):
        self.animation()

        if self.speed > 0:
            newpos = Math.movepos(self.rect.x, self.rect.y, self.endX, self.endY, self.speed)
            self.rect.x = newpos[0][0]
            self.rect.y = newpos[0][1]
            self.complete = newpos[1]
        else:
            self.rect.x = self.endX
            self.rect.y = self.endY

        self.entityCollision()
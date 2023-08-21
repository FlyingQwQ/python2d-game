import pygame
import time
import magic2d.resouces
from pygame.math import *
from magic2d.util import Math

class CycloneMagic(pygame.sprite.Sprite):

    sf = 160
    endX = 0
    endY = 0
    speed = 0
    complete = False

    # 攻击力
    hurt = 20

    def __init__(self):
        super().__init__()

        self.image = pygame.transform.scale(magic2d.resouces.magic1Frame[0], (695 - self.sf * 2 + 50, 454 - self.sf))
        self.rect = self.image.get_rect()

    '''
        技能动画播放
    '''
    frameIndex = 1
    moveAnimaTime = 0
    def animation(self):
        currTime = time.time()
        if currTime - self.moveAnimaTime > 0.1:
            self.frameIndex += 1
            if self.frameIndex > 17:
                self.frameIndex = 1
                self.complete = True
            self.image = pygame.transform.scale(magic2d.resouces.magic1Frame[self.frameIndex - 1], (695 - self.sf * 2 + 50, 454 - self.sf))
            self.moveAnimaTime = currTime

    '''
        设置攻击的开始位置和结束位置
    '''
    def setRoute(self, startX, startY, endX, endY):
        self.rect.x = startX
        self.rect.y = startY
        self.endX = endX
        self.endY = endY

    def setSpeed(self, speed):
        self.speed = speed

    def setWorld(self, worldObj):
        self.worldObj = worldObj

    '''
        碰到生物事件
    '''
    # 攻击CD时间
    cd = 0.3
    cdTime = 0
    def entityCollision(self):
        currTime = time.time()
        if (currTime - self.cdTime) > self.cd:
            for entity in pygame.sprite.spritecollide(self, self.worldObj.entityGroup, False):
                if entity.entityType != 'player':
                    entity.deductHealth(self.hurt)
            self.cdTime = currTime


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
import pygame
import time
import magic2d.resouces
import magic2d.world.block.air
from magic2d.util import ImageHandleTools

'''
    基本方块，所有方块都继承这个类的功能
'''
class BasicBlock():

    # 方块体积碰撞箱
    collision = False
    # 方块硬度
    hardness = 0
    # 是否开始挖掘
    isExcavate = False
    # 是否是液体方块
    liquid = False
    # 该方块对应的物品
    itemType = None
    # 方块是否开启灰度，开启后将会覆盖一层灰色，只对背景方块有效
    grayscale = True

    def __init__(self):
        pass

    '''
        设置方块位置
    '''
    def setLocation(self, x, y):
        self.rect.x = x
        self.rect.y = y
        self.worldX = int(x / 30)
        self.worldY = int(y / 30)

    '''
        设置方块所在世界
    '''
    def setWorld(self, worldObj):
        self.world = worldObj

    '''
        开始挖掘方块
    '''
    def startExcavate(self):
        player = self.world.getPlayer()
        self.isExcavate = True
        self.excavationLevel = player.getItemBox().getCurrItem().excavationLevel

    '''
        停止挖掘方块
    '''
    def endExcavate(self):
        self.isExcavate = False
        if self.imgfile:
            self.image.blit(self.imgfile, (0, 0))
            self.frameIndex = 0

    '''
        破坏方块动画
        继承该类后一定要调用这个方法，不然将会无法挖掘方块
    '''
    frameIndex = 0
    moveAnimaTime = 0
    def destroyAnima(self):
        if self.isExcavate and self.hardness != -1:
            currTime = time.time()
            if (self.hardness - self.excavationLevel) <= 0:
                self.hardness = 0
                self.excavationLevel = 0
            if currTime - self.moveAnimaTime > ((self.hardness - self.excavationLevel) * 0.1) / 8:
                if self.frameIndex >= 8:
                    # 挖掘完成
                    self.hardness = -1
                    if self.itemType:
                        self.world.spawnFallingBlockType(self.worldX, self.worldY, self.itemType)
                    newBlock = magic2d.world.block.air.Air()
                    self.world.setBlock(newBlock, self.worldX, self.worldY)
                else:
                    self.frameIndex += 1
                self.moveAnimaTime = currTime
            self.image.blit(self.imgfile, (0, 0))
            self.image.blit(ImageHandleTools.scale(magic2d.resouces.destroyBlockFrame[self.frameIndex], 30, 30), (0, 0))
import pygame
import time
import math
import magic2d.resouces
from magic2d.entity.enum.directionstate import DirectionState
from magic2d.entity.enum.movestate import MoveState

'''
    所有实体的基础类
'''
class EntityLive:

    entityType = None

    directionState = DirectionState.WAIT
    moveState = MoveState.RIGHT

    # 跳跃力
    jumpPower = 0
    gravity = 0.3
    stepY = 0

    stepX = 0
    velocityX = 0

    # 生物的最大移动速度
    maxSpeed = 3
    # 生物的当前移动速度
    speed = 3
    # 生命值 按百分之百算
    health = 100
    # 攻击力
    hurt = 0

    # 每帧的延迟，已秒为单位
    frameAnimationsDelay = 0
    # 帧数
    frameAnimationsNumber = 0
    # 帧动画左边
    frameAnimationsLeft = None
    # 帧动画右边
    frameAnimationsRight = None

    def __init__(self):
        pass

    def setWorld(self, worldObj):
        self.worldObj = worldObj

    '''
        设置主游戏画布
    '''
    def setSurface(self, surface:pygame.Surface):
        self.gameSurface = surface

    '''
        扣除实体生物血量按百分之百算
        以及删除实体
    '''
    def deductHealth(self, health):
        if (self.health - health) <= 0:
            if self.entityType != 'player':
                self.worldObj.removeEntity(self)
            else:
                self.worldObj.spawnPlayer()
        else:
            self.health -= health

    '''
        获取当前区块
    '''
    def getCurrChunk(self):
        currChunk = (self.rect.x / 30) / (len(self.worldObj.chunks) * 40) * len(self.worldObj.chunks)  # 当前区块
        currChunk = math.ceil(currChunk)

        return currChunk - 1

    def getLocation(self):
        return self.rect.x / 30, self.rect.y / 30

    '''
        更新实体移动贴图
    '''
    frameIndex = 0
    moveAnimaTime = 1
    def modelUpdate(self):
        currTime = time.time()
        if currTime - self.moveAnimaTime > self.frameAnimationsDelay:
            if self.moveState == MoveState.LEFTWALK:
                self.frameIndex += 1
                if self.frameIndex > self.frameAnimationsNumber:
                    self.frameIndex = 0
                self.image = self.frameAnimationsLeft[self.frameIndex]
            elif self.moveState == MoveState.RIGHTWALK:
                self.frameIndex += 1
                if self.frameIndex > self.frameAnimationsNumber:
                    self.frameIndex = 0
                self.image = self.frameAnimationsRight[self.frameIndex]

            # 修改完贴图需要重新设置碰撞箱，不然会出问题
            newRect = self.image.get_rect()
            self.rect.width = newRect.width
            self.rect.height = newRect.height
            self.moveAnimaTime = currTime

            if self.moveState == MoveState.LEFT:
                self.image = self.frameAnimationsLeft[0]
            elif self.moveState == MoveState.RIGHT:
                self.image = self.frameAnimationsRight[0]

    def actionUpdate(self):
        self.stepX += self.velocityX

        if self.stepX > self.speed:
            self.velocityX = self.speed
            self.stepX = self.speed
        elif self.stepX < 0 - self.speed:
            self.velocityX = 0 - self.speed
            self.stepX = 0 - self.speed

        if self.moveState == MoveState.RIGHT:
            if self.stepX > 0:
                self.velocityX = -0.5
            else:
                self.velocityX = 0
                self.stepX = 0
        elif self.moveState == MoveState.LEFT:
            if self.stepX < 0:
                self.velocityX = 0.5
            else:
                self.velocityX = 0
                self.stepX = 0

        if self.directionState == DirectionState.JUMP:
            self.jumpPower += self.gravity
        self.stepY = self.jumpPower

    '''
        生物AI
    '''
    def aiUpdate(self):
        pass

    '''
        生物AI跟随跳跃
    '''
    def aiFollowJump(self, world, player):
        entityX, entityY = self.getLocation()
        playerX, playerY = player.getLocation()
        if playerX < entityX:
            frontBlock = world.getBlock(int(entityX) - 1, int(entityY + 1))
            if frontBlock:
                if frontBlock.collision:
                    head_front_Block = world.getBlock(int(entityX) - 1, int(entityY))
                    if not head_front_Block.collision:
                        if self.directionState != DirectionState.JUMP:
                            self.directionState = DirectionState.JUMP
                            self.jumpPower = -5
        elif playerX > entityX:
            frontBlock = world.getBlock(int(entityX) + 1, int(entityY + 1))
            if frontBlock:
                if frontBlock.collision:
                    head_front_Block = world.getBlock(int(entityX) + 1, int(entityY))
                    if not head_front_Block.collision:
                        if self.directionState != DirectionState.JUMP:
                            self.directionState = DirectionState.JUMP
                            self.jumpPower = -5

    '''
        接触玩家触发事件
    '''
    def contactPlayer(self, playerObj):
        pass
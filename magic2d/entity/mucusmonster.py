import pygame
import time
import magic2d.util.Math
import magic2d.resouces
import magic2d.entity.entitylive
from magic2d.entity.enum.directionstate import DirectionState
from magic2d.entity.enum.movestate import MoveState


class MucusMonster(pygame.sprite.Sprite, magic2d.entity.entitylive.EntityLive):

    entityType = 'monster'
    maxSpeed = 2
    hurt = 15

    def __init__(self, x, y):
        super().__init__()
        self.image = magic2d.resouces.monster1LeftFrame[1]
        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.frameAnimationsDelay = 0.3
        # 帧数
        self.frameAnimationsNumber = 1
        # 帧动画左边
        self.frameAnimationsLeft = magic2d.resouces.monster1LeftFrame
        # 帧动画右边
        self.frameAnimationsRight = magic2d.resouces.monster1RightFrame


    playerDirection = 'wait'
    def aiUpdate(self):
        world = self.worldObj
        player = world.getPlayer()
        playerX, playerY = player.getLocation()
        entityX, entityY = self.getLocation()

        distance = magic2d.util.Math.poslen(playerX, playerY, entityX, entityY)
        if distance < 10:
            if playerX < entityX:
                if self.playerDirection != 'left':
                    self.moveState = MoveState.LEFTWALK
                    self.velocityX = -0.2
                    self.stepX = -0.2
                    self.playerDirection = 'left'
                self.aiFollowJump(world, player)
            elif playerX > entityX:
                if self.playerDirection != 'right':
                    self.moveState = MoveState.RIGHTWALK
                    self.velocityX = 0.2
                    self.stepX = 0.2
                    self.playerDirection = 'right'
                self.aiFollowJump(world, player)
        else:
            if self.playerDirection != 'wait':
                self.velocityX = 0
                self.stepX = 0
                self.playerDirection = 'wait'
                if self.moveState == MoveState.LEFTWALK:
                    self.moveState = MoveState.LEFT
                elif self.moveState == MoveState.RIGHTWALK:
                    self.moveState = MoveState.RIGHT

    #攻击CD时间
    cd = 1.5
    cdTime = 0
    def contactPlayer(self, playerObj):
        currTime = time.time()
        if (currTime - self.cdTime) > self.cd:

            playerObj.jumpPower = -4
            playerObj.directionState = DirectionState.JUMP
            playerObj.deductHealth(self.hurt)

            self.cdTime = currTime

    def update(self):

        self.actionUpdate()
        self.modelUpdate()
        self.aiUpdate()
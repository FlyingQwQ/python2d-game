import pygame
import math
import magic2d.util.Math
import magic2d.world.blockconfig
from magic2d.item import *
from magic2d.entity import *
from magic2d.world.chunk import *
from magic2d.world.decoration import armshouse
from magic2d.entity.enum.directionstate import DirectionState
from magic2d.entity.enum.movestate import MoveState


class MainWorld:

    chunks = [plainterrain, snowterrain, plainterrain]
    displayRegion = []  #前景方块
    backgroundRegion = []   #背景方块
    entitys = [] #实体列表

    '''
        width: 世界宽度
        height: 世界高度
    '''
    def __init__(self, width, height):
        #世界背景
        self.background = pygame.Surface((1000, 600))
        #世界
        self.world = pygame.Surface((width, height))
        self.world.set_colorkey(pygame.Color(255, 255, 255))
        #相机
        self.cameraRect = pygame.Surface((1000, 600)).get_rect()

        #初始化实体精灵组
        self.entityGroup = pygame.sprite.Group()
        #初始化魔法精灵组
        self.magicGroup = pygame.sprite.Group()
        #初始化装饰精灵组
        self.decorationGroup = pygame.sprite.Group()
        #前景方块精灵组
        self.blockGroup = pygame.sprite.Group()
        #背景方块精灵组
        self.backgroundBlockGroup = pygame.sprite.Group()

        self.initDecoration()
        self.initEntity()
        self.__floorSplicing()

    '''
        实时获取玩家位置当前的区块
        绘制背景，如果使用带有透明文件尺寸过大会导致帧数暴跌
        尽量压缩
    '''
    beforeChunk = -1
    beforeTick = 0
    switchBackground = False
    backgroundFrame = 0
    def falshChunk(self):
        player = self.getPlayer()
        currChunk = player.getCurrChunk()
        if currChunk != self.beforeChunk:
            self.switchBackground = True
            self.beforeChunk = currChunk
            self.backgroundFrame = 0

        if self.switchBackground:
            if pygame.time.get_ticks() - self.beforeTick > 30:
                if self.backgroundFrame >= 255:
                    self.switchBackground = False
                else:
                    backgroundImage = pygame.transform.scale(self.chunks[currChunk].background, (1000, 600))
                    backgroundImage.set_alpha(self.backgroundFrame)
                    self.background.blit(backgroundImage, (0, 0))
                    self.backgroundFrame += 30
                self.beforeTick = pygame.time.get_ticks()


    '''
        将多个区块进行拼接，包括前景以及背景
        每个区块的高度和宽度限定40格
    '''
    def __floorSplicing(self):
        self.displayRegion.clear()
        self.backgroundRegion.clear()
        for y in range(40):
            newLine = []
            backgroundNewLine = []
            for chunkList in self.chunks:
                newLine += chunkList.blockList[y]
                backgroundNewLine += chunkList.backgroundBlockList[y]
            self.displayRegion.append(newLine)
            self.backgroundRegion.append(backgroundNewLine)

    '''
        绘制玩家周围一定数量的方块，可以提升游戏性能
    '''
    startX = 0
    endX = 0
    startY = 0
    endY = 0
    def drawFloor(self):
        self.blockGroup.empty()
        self.backgroundBlockGroup.empty()

        blockList = self.displayRegion
        backgroundBlockList = self.backgroundRegion

        currY = self.startY
        currX = self.startX
        for y in range(self.startY, self.endY):
            for x in range(self.startX, self.endX):
                blockId = blockList[y][x]
                backgroundBlockId = backgroundBlockList[y][x]
                newBlock = magic2d.world.blockconfig.createBlock(blockId, currX, currY)
                newBlock.setWorld(self)
                self.blockGroup.add(newBlock)

                backgroundBlock = magic2d.world.blockconfig.createBlock(backgroundBlockId, currX, currY)
                if backgroundBlock.grayscale:
                    mask = pygame.Surface((backgroundBlock.rect.width, backgroundBlock.rect.height)) #创建黑色遮罩
                    mask.set_alpha(120)
                    backgroundBlock.image.blit(mask, (0, 0))
                self.backgroundBlockGroup.add(backgroundBlock)
                currX += 1
            currX = self.startX
            currY += 1

    '''
        获取鼠标世界位置
    '''
    def getMousePos(self):
        mouseX = pygame.mouse.get_pos()[0] + self.cameraRect.x
        mouseY = pygame.mouse.get_pos()[1] + self.cameraRect.y
        blockX = int(mouseX / 30)
        blockY = int(mouseY / 30)
        return blockX, blockY

    '''
        获取鼠标当前区块
    '''
    def getMouseChunk(self):
        mouseX = pygame.mouse.get_pos()[0] + self.cameraRect.x
        currChunk = round(mouseX / 30) / (len(self.chunks) * 39) * len(self.chunks)  # 当前区块
        currChunk = math.ceil(currChunk)
        return currChunk - 1

    '''
        获取世界坐标方块实例
    '''
    def getBlock(self, x, y):
        if y >= 40:
            y = 39
        if x >= len(self.displayRegion[0]):
            x = len(self.displayRegion[0]) - 1
        for block in self.blockGroup:
            if block.worldX == x and block.worldY == y:
                return block
        return None

    '''
        获取物品栏放置方块
    '''
    def placeBlock(self, worldX, worldY):
        block = self.getBlock(worldX, worldY)
        if block.__class__.__name__ == 'Air' or block.liquid:
            upBlock = self.getBlock(worldX, worldY - 1)
            bottomBlock = self.getBlock(worldX, worldY + 1)
            leftBlock = self.getBlock(worldX - 1, worldY)
            rightBlock = self.getBlock(worldX + 1, worldY)

            if upBlock.collision or bottomBlock.collision or leftBlock.collision or rightBlock.collision:
                player = self.getPlayer()
                itemBox = player.getItemBox()
                newblock = itemBox.buildBlock()
                newblock.collision = True
                if newblock:
                    itemBox.useItem()
                    if worldY < 40 and worldX < len(self.displayRegion[0]):
                        self.setBlock(newblock, worldX, worldY)

    '''
        使用世界坐标设置方块
    '''
    def setBlock(self, blockObj, x, y):
        oldBlock = self.getBlock(x, y)
        blockObj.setLocation(oldBlock.rect.x, oldBlock.rect.y)
        self.displayRegion[y][x] = blockObj.blockId
        self.drawFloor()

    '''
        初始化生成实体
    '''
    def initEntity(self):
        pass

    '''
        初始化生成装饰
    '''
    def initDecoration(self):
        armsHouse = armshouse.ArmsHouse(60, 222)
        self.addDecoration(armsHouse)

    '''
        获取世界实体
    '''
    def getEntitys(self):
        return self.blockGroup

    '''
        添加实体
    '''
    def addEntity(self, entity):
        entity.setSurface(self.gameSurface)
        entity.setWorld(self)
        self.entityGroup.add(entity)
        self.entitys.append(entity)

    '''
        删除实体
    '''
    def removeEntity(self, entityObj):
        self.entityGroup.remove(entityObj)
        self.entitys.remove(entityObj)

    '''
        根据方块类型生成凋落物
    '''
    def spawnFallingBlockType(self, x, y, itemType):
        newFalling = falling.Falling()
        newFalling.setLocation(x, y)
        itemObj = eval(itemType + '()')
        newFalling.setItem(itemObj)
        self.addEntity(newFalling)

    '''
        根据物品实例生成掉落物
    '''
    def spawnFallingItemObj(self, x, y, itemObj):
        newFalling = falling.Falling()
        newFalling.setLocation(x, y)
        newFalling.setItem(itemObj)
        self.addEntity(newFalling)

    '''
        玩家重生
    '''
    def spawnPlayer(self):
        player = self.getPlayer()
        player.health = 100
        player.rect.x = 20
        player.rect.y = 250
        player.moveState = MoveState.RIGHT
        self.cameraRect.x = 0
        self.cameraRect.y = 0
        self.endX = 0

    '''
        获取实体世界坐标
    '''
    def getEntityWorldLocation(self, entityObj):
        return round(entityObj.rect.x / 30), int(entityObj.rect.y / 30)

    '''
        获取玩家实例
    '''
    def getPlayer(self):
        for entity in self.entityGroup.sprites():
            if entity.entityType == 'player':
                return entity
        return None

    '''
        生成特效
    '''
    def sendMagic(self, magicObj, startX, startY, endX, endY):
        magicObj.setRoute(startX, startY, endX, endY)
        magicObj.setWorld(self)
        self.magicGroup.add(magicObj)

    '''
        添加装饰
    '''
    def addDecoration(self, decorationObj):
        self.decorationGroup.add(decorationObj)

    '''
        设置主游戏画布
    '''
    def setSurface(self, surface:pygame.Surface):
        self.gameSurface = surface

    '''
        加载实体，距离玩家x内的距离内加载实体
    '''
    def entityLoad(self):
        playerX, playerY = self.getPlayer().getLocation()
        for entity in self.entitys:
            if entity.entityType != 'player':
                entityX, entityY = entity.getLocation()
                distance = magic2d.util.Math.poslen(playerX, playerY, entityX, entityY)
                if distance >= 17:
                    self.entityGroup.remove(entity)
                else:
                    if entityY > playerY - 10 and entityY < playerY + 5:
                        self.entityGroup.add(entity)
                    else:
                        self.entityGroup.remove(entity)

    '''
        方块碰撞检测
    '''
    def collision(self, group):
        for entity in self.entityGroup:

            # 边境检测，防止实体过界
            if (entity.rect.x / 30) >= len(self.displayRegion[0]) - 1:
                entity.rect.x = (len(self.displayRegion[0])) * 30 - (1 * 30)
            elif entity.rect.x < 8:
                entity.rect.x = 8

            # 检测实体底下的方块是不是可碰撞方块，不是的话自然掉落
            if entity.entityType != 'falling':
                footBlock = self.getBlock(round(entity.rect.x / 30), int(entity.rect.y / 30) + 2)  # 获取实体下的方块
                if footBlock:
                    if not footBlock.collision:
                        entity.directionState = DirectionState.JUMP
            else:
                entity.rect.y += 1
                footBlock = pygame.sprite.spritecollideany(entity, group)
                if footBlock:
                    if not footBlock.collision:
                        entity.directionState = DirectionState.JUMP
                entity.rect.y -= 1

            # 检测实体有没有在水里
            bodyBlock = self.getBlock(round(entity.rect.x / 30), int(entity.rect.y / 30) + 1)  # 获取实体下的方块
            if bodyBlock:
                if bodyBlock.liquid:
                    entity.speed = 2
                    entity.gravity = 0.2
                else:
                    entity.speed = entity.maxSpeed
                    entity.gravity = 0.4

            entity.rect.y += entity.stepY
            blocks = pygame.sprite.spritecollide(entity, group, False)
            if blocks:
                for block in blocks:
                    if block.collision:
                        if entity.stepY > 0:
                            entity.rect.bottom = block.rect.top
                            entity.stepY = 0
                            entity.jumpPower = 0
                            entity.directionState = DirectionState.WAIT
                        else:
                            entity.rect.top = block.rect.bottom
                        break

            entity.rect.x += entity.stepX
            blocks = pygame.sprite.spritecollide(entity, group, False)
            if blocks:
                for block in blocks:
                    if block.collision:
                        if entity.stepX > 0:
                            entity.rect.right = block.rect.left
                        else:
                            entity.rect.left = block.rect.right
                        break

    '''
        生物碰到玩家事件
    '''
    def entityCollision(self):
        player = self.getPlayer()
        for entity in pygame.sprite.spritecollide(player, self.entityGroup, False):
            if entity.entityType != 'player':
                entity.contactPlayer(player)

    enterXFrontierEnd = False
    enterYFrontierEnd = False
    def update(self):
        self.world.fill(color=(255, 255, 255))
        self.gameSurface.blit(self.background, (0, 0))

        self.entityLoad()

        #绘制玩家附近的地形
        player = self.getPlayer()
        playerX, playerY = self.getEntityWorldLocation(player)
        if player.rect.x < self.cameraRect.width / 2:
            if playerX > self.endX - 17:
                self.startX = 0
                self.endX = playerX + 30
                self.drawFloor()
        else:
            if (playerX + 18) < len(self.displayRegion[0]):
                if playerX < self.startX + 17 or playerX > self.endX - 17:
                    self.endX = playerX + 18
                    self.startX = playerX - 18
                    self.drawFloor()
                    self.enterXFrontierEnd = True
            else:
                if self.enterXFrontierEnd:
                    self.startX = playerX - 30
                    self.endX = len(self.displayRegion[0])
                    self.drawFloor()
                    self.enterXFrontierEnd = False

        if (playerY < 41 - 7):
            if playerY < self.startY + 10 or playerY > self.endY - 7:
                self.startY = playerY - 17
                self.endY = playerY + 8
                self.drawFloor()
                self.enterYFrontierEnd = True
        else:
            if self.enterYFrontierEnd:
                self.startY = playerY - 17
                self.endY = 40
                self.drawFloor()
                self.enterYFrontierEnd = False

        self.falshChunk()

        self.backgroundBlockGroup.draw(self.world)
        self.blockGroup.draw(self.world)
        self.decorationGroup.draw(self.world)
        self.entityGroup.draw(self.world)
        self.magicGroup.draw(self.world)

        self.decorationGroup.update()
        self.entityGroup.update()
        self.magicGroup.update()
        self.backgroundBlockGroup.update()
        self.blockGroup.update()

        self.collision(self.blockGroup)
        self.entityCollision()

        for entity in self.entityGroup.sprites():
            if entity.entityType == 'player':
                if entity.rect.x > self.cameraRect.width / 2:
                    self.cameraRect.x = entity.rect.x - (self.cameraRect.width / 2)
                self.cameraRect.y = entity.rect.y - (self.cameraRect.height / 2) - 120

        # 检测魔法是否完成，完成消除魔法
        for magic in self.magicGroup.sprites():
            if magic.complete:
                self.magicGroup.remove(magic)

        self.gameSurface.blit(self.world, (0, 0), self.cameraRect)
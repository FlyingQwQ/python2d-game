import pygame
import magic2d.resouces
from magic2d.item import *
from magic2d.world.block import *
from magic2d.util import ImageHandleTools


class ItemBox(pygame.sprite.Sprite):

    itemList = [0] * 7
    itemNumberList = [0] * 7
    currItemIndex = 0

    def __init__(self, x, y):
        super().__init__()
        self.itemboxImage = ImageHandleTools.widthScale(magic2d.resouces.itemBox, 330)
        self.selectItemImage = ImageHandleTools.widthScale(magic2d.resouces.selectItemFrame, 42)

        self.image = pygame.Surface((self.itemboxImage.get_width(), self.itemboxImage.get_height()))
        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.font = pygame.font.SysFont("宋体", 18)

        sitem = stoneblockitem.StoneBlockItem()
        self.setItem(sitem, 6)
        self.setItemNumber(6, 64)
        gitem = wood_pickaxe.WoodPickaxe()
        self.setItem(gitem, 1)
        Cyclonestaffitem = cyclonestaffitem.CycloneStaffItem()
        self.setItem(Cyclonestaffitem, 2)
        arms1 = arms1item.Arms1Item()
        self.setItem(arms1, 0)

    '''
        设置指定位置的物品
    '''
    def setItem(self, itemObj, index):
        self.itemList[index] = itemObj

    '''
        添加新的物品到物品栏
    '''
    def addItem(self, itemObj):
        newItem = eval(itemObj.itemClass + '()')
        for index, item in enumerate(self.itemList):
            if item != 0:
                if item.__class__.__name__ == newItem.__class__.__name__:
                    self.itemNumberList[index] += 1
                    break
        else:
            for index, item in enumerate(self.itemList):
                if item == 0:
                    self.itemList[index] = newItem
                    self.itemNumberList[index] += 1
                    break
            else:
                return False
        return True

    def useItem(self):
        index = self.getCurrItemindex()
        itemNumber = self.getItemNumber(index)
        if itemNumber - 1 <= 0:
            self.removeItem(index)
        self.setItemNumber(index, itemNumber - 1)


    '''
        移除指定位置的物品
    '''
    def removeItem(self, index):
        self.itemList[index] = 0
        self.setItemNumber(index, 0)

    '''
        设置指定位置的物品数量
    '''
    def setItemNumber(self, index, number):
        self.itemNumberList[index] = number

    '''
        获取指定位置的物品数量
    '''
    def getItemNumber(self, index):
        return self.itemNumberList[index]

    '''
        设置当前手持物品的位置
    '''
    def setCurrItemindex(self, index):
        if index < 0:
            index = 0
        elif index > 6:
            index = 6
        self.currItemIndex = index
        currItem = self.getCurrItem()
        if currItem != 0:
            self.selectBlockFrame.setVisible(currItem.selectIndicatorVisible)
        else:
            self.selectBlockFrame.setVisible(False)

    '''
        获取当前手持物品的位置
    '''
    def getCurrItemindex(self):
        return self.currItemIndex

    '''
        获取当前手持物品的实例
    '''
    def getCurrItem(self):
        return self.itemList[self.getCurrItemindex()]

    '''
        获取当前手持物品实例来构建方块
    '''
    def buildBlock(self):
        item = self.getCurrItem()
        if item != 0:
            if item.itemType == 'block':
                return eval(item.blockType + '()')
        return None

    '''
        设置选择指示器
    '''
    def setSelectIndicator(self, selectBlockFrame):
        self.selectBlockFrame = selectBlockFrame

    def update(self):
        self.image.fill((127, 140, 141))
        self.image.set_colorkey((127, 140, 141))
        self.image.blit(self.itemboxImage, (0, 0))

        for index, itemObj in enumerate(self.itemList):
            if itemObj != 0:
                self.image.blit(itemObj.image, ((3 + (42 * index) + (5 * index)) + ((42 / 2) - (itemObj.image.get_rect().width / 2)), ((42 / 2) - (itemObj.image.get_rect().width / 2) + 3)))
                if itemObj.stackable:
                    itemNumber = self.font.render(str(self.getItemNumber(index)), True, pygame.Color(255, 255, 255))
                    self.image.blit(itemNumber, (8 + (42 * index) + (5 * index), 28))

        self.image.blit(self.selectItemImage, (3 + (42 * self.currItemIndex) + (5 * self.currItemIndex), 2))

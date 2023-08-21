import pygame


'''
    基本物品，所有物品都继承这个类的功能
'''
class BasicItem:

    #物品类型
    itemType = None
    #物品的类路径
    itemClass = None
    #方块类型，物品类型需要block才会起作用
    blockType = None
    #是否开启选择指示器
    selectIndicatorVisible = False
    #物品是否可以堆叠
    stackable = True
    #物品的使用范围有多大
    range = 5

    def __init__(self):
        pass

    def getBlockType(self):
        return self.itemType

    '''
        玩家在世界使用物品的时候触发
    '''
    def useItem(self, worldObj):
        pass
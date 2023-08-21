import pygame
import random
import magic2d.util.ImageHandleTools
import magic2d.entity.entitylive

'''
    掉落物实体
'''
class Falling(pygame.sprite.Sprite, magic2d.entity.entitylive.EntityLive):

    entityType = 'falling'

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((0, 0))
        self.rect = self.image.get_rect()

    def setItem(self, itemObj):
        self.itemObj = itemObj
        self.image = magic2d.util.ImageHandleTools.scale(itemObj.image, itemObj.handImageWidth, itemObj.handImageHeight)
        x = self.rect.x
        y = self.rect.y
        self.rect = self.image.get_rect()
        self.rect.x = (x * 30) + random.randint(3, 15)
        self.rect.y = y * 30
        pygame.draw.rect(self.image, (189, 195, 199), (0, 0, self.rect.width, self.rect.height), 1)

    def setLocation(self, x, y):
        self.rect.x = x
        self.rect.y = y

    '''
        检测玩家是否碰到掉落物
    '''
    def collision(self):
        player = self.worldObj.getPlayer()
        if pygame.sprite.collide_rect(player, self):
            itemBox = player.getItemBox()
            if itemBox.addItem(self.itemObj):
                self.worldObj.removeEntity(self)

    def update(self):
        self.collision()
        self.actionUpdate()
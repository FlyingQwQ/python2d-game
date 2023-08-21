import pygame
import magic2d.resouces
from magic2d.util import ImageHandleTools

class SelectBlockFrame(pygame.sprite.Sprite):

    visible = False

    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.set_colorkey(pygame.Color(0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def setWorld(self, worldObj):
        self.worldObj = worldObj

    def setVisible(self, visible):
        self.visible = visible
        if self.visible:
            self.image = ImageHandleTools.scale(magic2d.resouces.selectBlockFrame, 30, 30)
        else:
            self.image.fill(pygame.Color(0, 0, 0))
            self.image.set_colorkey(pygame.Color(0, 0, 0))

    def update(self):
        mouseX = pygame.mouse.get_pos()[0] + self.worldObj.cameraRect.x
        mouseY = pygame.mouse.get_pos()[1] + self.worldObj.cameraRect.y

        blockX = int(mouseX / 30)
        blockY = int(mouseY / 30)

        self.rect.x = (blockX * 30) - self.worldObj.cameraRect.x
        self.rect.y = (blockY * 30) - self.worldObj.cameraRect.y
import pygame

'''
    鼠标精灵
'''
class MouseSp(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((5, 5))
        self.image.set_colorkey((0, 0, 0))
        self.rect = self.image.get_rect()

    '''
        设置鼠标精灵位置
    '''
    def setLocation(self, x, y):
        self.rect.x = x - (self.image.get_width() / 2)
        self.rect.y = y - (self.image.get_height() / 2)
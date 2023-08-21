import pygame

class Button(pygame.sprite.Sprite):

    def __init__(self, x, y, text):
        super().__init__()
        self.image = pygame.Surface((250, 60))
        self.image.fill((112, 128, 144))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.text = text
        self.font = pygame.font.Font('./resouces/font/xs.ttf', 18)

    '''
        添加事件回调
    '''
    def addEvent(self, listener):
        self.listener = listener

    '''
        系统调用事件
    '''
    def exec_listener(self):
        try:
            return self.listener()
        except AttributeError:
            pass

    '''
        鼠标进入事件
    '''
    def mouseEnter(self):
        self.image.fill((0, 100, 0))

    '''
        鼠标退出事件
    '''
    def mouseOver(self):
        self.image.fill((112, 128, 144))

    def update(self):
        buttonText = self.font.render(self.text, True, pygame.Color(255, 255, 255))
        self.image.blit(buttonText, (125 - (buttonText.get_width() / 2), 30 - (buttonText.get_height() / 2)))
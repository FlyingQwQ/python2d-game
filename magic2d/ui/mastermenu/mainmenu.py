import pygame
import magic2d.resouces
import magic2d.ui.mastermenu.button
from magic2d.util import ImageHandleTools

'''
    游戏主菜单
'''
class MainMenu:

    def __init__(self):
        self.image = ImageHandleTools.widthScale(magic2d.resouces.mainMenuTitle, 400)
        self.background = ImageHandleTools.widthScale(pygame.transform.rotate(magic2d.resouces.masterBackground, 10), 1500)

        self.widgetGroup = pygame.sprite.Group()

        # 游戏开始按钮
        startButton = magic2d.ui.mastermenu.button.Button(500 - (250 / 2), 230, '开始游戏')
        startButton.addEvent(self.startGame)
        # 关闭游戏按钮
        exitButton = magic2d.ui.mastermenu.button.Button(500 - (250 / 2), 310, '返回桌面')
        exitButton.addEvent(self.exitGame)

        self.widgetGroup.add(startButton)
        self.widgetGroup.add(exitButton)

    def setSurface(self, surface:pygame.Surface):
        self.surface = surface

    '''
        鼠标点击事件
    '''
    def mouseClick(self, mouseSp):
        widgets = pygame.sprite.spritecollide(mouseSp, self.widgetGroup, False)
        if widgets:
            for widget in widgets:
                return widget.exec_listener()

    '''
        鼠标移入退出事件
    '''
    currWidget = None
    def mouseMotion(self, mouseSp):
        widgets = pygame.sprite.spritecollide(mouseSp, self.widgetGroup, False)
        if widgets:
            if not self.currWidget:
                self.currWidget = widgets[0]
                self.currWidget.mouseEnter()
            pygame.mouse.set_cursor(pygame.cursors.broken_x)
        else:
            if self.currWidget != None:
                self.currWidget.mouseOver()
                self.currWidget = None
            pygame.mouse.set_cursor(pygame.cursors.arrow)

    def update(self):
        self.surface.blit(self.background, (-130, -220))
        self.surface.blit(self.image, (300, 80))

        self.widgetGroup.draw(self.surface)
        self.widgetGroup.update()

    def startGame(self):
        return 1

    def exitGame(self):
        return 2
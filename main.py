import pygame
import magic2d.util.Math
import magic2d.ui.mousesp
import magic2d.ui.mastermenu.mainmenu
from magic2d.ui import *
from magic2d.world import mainworld
from magic2d.entity.player import Player
from magic2d.entity.mucusmonster import MucusMonster
from magic2d.entity.enum.directionstate import DirectionState
from magic2d.entity.enum.movestate import MoveState
from magic2d.magic import magic2

exit = False
currMouseBlock = None
isStartGame = False

def event_process():
    global isStartGame
    #游戏是否退出
    global exit
    #当前鼠标指向的方块
    global currMouseBlock

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if isStartGame:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    player.moveState = MoveState.RIGHTWALK
                    player.velocityX = 0.2
                    player.stepX = 0.2
                elif event.key == pygame.K_a:
                    player.moveState = MoveState.LEFTWALK
                    player.velocityX = -0.2
                    player.stepX = -0.2
                elif event.key == pygame.K_SPACE or event.key == pygame.K_w:
                    if player.directionState != DirectionState.JUMP:
                        player.directionState = DirectionState.JUMP
                        player.jumpPower = -5
                elif event.key == pygame.K_x:
                    world.spawnPlayer()
                elif event.key == pygame.K_q:
                    # 丢出物品
                    item = itemBoxObj.getCurrItem()
                    if item != 0:
                        playerX, playerY = player.getLocation()
                        handItem.setVisible(True)
                        if player.moveState == MoveState.LEFTWALK or player.moveState == MoveState.LEFT:
                            world.spawnFallingItemObj(playerX - 1, playerY, item)
                        elif player.moveState == MoveState.RIGHTWALK or player.moveState == MoveState.RIGHT:
                            world.spawnFallingItemObj(playerX + 1, playerY, item)
                        itemBoxObj.useItem()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    player.moveState = MoveState.RIGHT
                if event.key == pygame.K_a:
                    player.moveState = MoveState.LEFT
            elif event.type == pygame.MOUSEMOTION:
                mouseX = pygame.mouse.get_pos()[0] + world.cameraRect.x
                mouseY = pygame.mouse.get_pos()[1] + world.cameraRect.y
                blockX = int(mouseX / 30)
                blockY = int(mouseY / 30)

                block = world.getBlock(blockX, blockY)
                if currMouseBlock != None:
                    if currMouseBlock != block:
                        currMouseBlock.endExcavate()
                        currMouseBlock = block
                else:
                    currMouseBlock = block
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    mouseX = pygame.mouse.get_pos()[0] + world.cameraRect.x
                    mouseY = pygame.mouse.get_pos()[1] + world.cameraRect.y

                    blockX = int(mouseX / 30)
                    blockY = int(mouseY / 30)

                    item = itemBoxObj.getCurrItem()
                    if item != 0:
                        playerX, playerY = player.getLocation()
                        if magic2d.util.Math.poslen(playerX, playerY, blockX, blockY) <= item.range:
                            handItem.setVisible(True)
                            item.useItem(world)
                elif pygame.mouse.get_pressed()[2]:
                    mouseX = pygame.mouse.get_pos()[0] + world.cameraRect.x
                    mouseY = pygame.mouse.get_pos()[1] + world.cameraRect.y

                    blockX = int(mouseX / 30)
                    blockY = int(mouseY / 30)

                    item = itemBoxObj.getCurrItem()
                    if item != 0:
                        if item.itemType == 'block':
                            if not pygame.sprite.spritecollide(world.getBlock(blockX, blockY), world.entityGroup, False):
                                playerX, playerY = player.getLocation()
                                if magic2d.util.Math.poslen(playerX, playerY, blockX, blockY) <= 5:
                                    world.placeBlock(blockX, blockY)

                                    handItem.setVisible(True)
                elif event.button == 4:
                    itemBoxObj.setCurrItemindex(itemBoxObj.getCurrItemindex() - 1)
                elif event.button == 5:
                    itemBoxObj.setCurrItemindex(itemBoxObj.getCurrItemindex() + 1)
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if currMouseBlock:
                        currMouseBlock.endExcavate()
                elif event.button == 3:
                    handItem.setVisible(False)
        else:
            if event.type == pygame.MOUSEMOTION:
                mouseX = pygame.mouse.get_pos()[0]
                mouseY = pygame.mouse.get_pos()[1]
                mouseSp.setLocation(mouseX, mouseY)
                mainMenu.mouseMotion(mouseSp)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]:
                    clickState = mainMenu.mouseClick(mouseSp)
                    if clickState:
                        if clickState == 1:
                            pygame.mouse.set_cursor(pygame.cursors.arrow)
                            isStartGame = True
                        elif clickState == 2:
                            exit = True

'''
    初始化UI
'''
def InitUI(world):
    global mouseGroup
    global mouseSp
    global mainMenu
    global itemBoxObj
    global handItem

    #鼠标精灵组
    mouseGroup = pygame.sprite.Group()
    mouseSp = magic2d.ui.mousesp.MouseSp()
    mouseGroup.add(mouseSp)

    # 创建游戏窗口主菜单
    mainMenu = magic2d.ui.mastermenu.mainmenu.MainMenu()
    mainMenu.setSurface(screen)

    selectBlockFrame = selectblockframe.SelectBlockFrame(300, 300)
    selectBlockFrame.setWorld(world)

    itemBoxObj = itembox.ItemBox(300, 10)
    itemBoxObj.setSelectIndicator(selectBlockFrame)

    handItem = handitem.HandItem()
    handItem.setWorld(world)
    handItem.setItemBox(itemBoxObj)

    ui.UIGroup.add(selectBlockFrame)
    ui.UIGroup.add(itemBoxObj)
    ui.UIGroup.add(handItem)

def main():
    global exit
    global player
    global world
    global UIGroup
    global screen

    pygame.init()
    pygame.display.init()
    screen = pygame.display.set_mode((1000, 600), pygame.HWSURFACE)
    pygame.display.set_caption('Magic2D v0.0.1 alpha')
    pygame.display.set_icon(pygame.image.load('./resouces/logo.png'))
    clock = pygame.time.Clock()

    # 创建世界
    world = mainworld.MainWorld(6000, 6000)
    world.setSurface(screen)

    InitUI(world)

    # 创建玩家将玩家添加到一个世界里
    player = Player(300, 0)
    player.setItemBox(itemBoxObj)
    player.setHandItem(handItem)
    world.addEntity(player)

    # 创建一个怪物添加到一个世界里
    mucusMonster = MucusMonster(1200, 120)
    world.addEntity(mucusMonster)
    # mucusMonster1 = MucusMonster(1200, 0)
    #world.addEntity(mucusMonster1)

    font = pygame.font.SysFont("宋体", 23)
    while not exit:
        clock.tick(60)
        event_process()

        if isStartGame:
            world.update()

            ui.UIGroup.draw(screen)
            ui.UIGroup.update()

            fpsText = font.render('FPS: ' + str(round(clock.get_fps())), True, pygame.Color(255, 255, 255))
            screen.blit(fpsText, (30, screen.get_height() - 30))
        else:
            mainMenu.update()

        mouseGroup.draw(screen)
        mouseGroup.update()

        pygame.display.update()
    pygame.quit()

if __name__ == '__main__':
    main()
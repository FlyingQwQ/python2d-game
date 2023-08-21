import pygame
from magic2d.util import ImageHandleTools

# -----世界素材，UI素材
masterBackground = pygame.image.load('./resouces/masterBackground.png')
mainMenuTitle = pygame.image.load('./resouces/title.png')
plainBackground = pygame.image.load('./resouces/plain.jpg')
snowBackground = pygame.image.load('./resouces/snow.jpg')
itemBox = pygame.image.load('./resouces/itembox.png')
selectItemFrame = pygame.image.load('./resouces/selectitem.png')
selectBlockFrame = pygame.image.load('./resouces/selectblock.png')

# -----玩家素材
playerImage = pygame.image.load('./resouces/entity/player.png')
playerRightFrame = []
playerRightFrame.append(ImageHandleTools.get_image(playerImage, 67, 99, 24, 44, pygame.Color(0, 255, 0)))
playerRightFrame.append(ImageHandleTools.get_image(playerImage, 98, 99, 24, 44, pygame.Color(0, 255, 0)))
playerRightFrame.append(ImageHandleTools.get_image(playerImage, 34, 100, 24, 44, pygame.Color(0, 255, 0)))
playerRightFrame.append(ImageHandleTools.get_image(playerImage, 0, 3, 30, 44, pygame.Color(0, 255, 0))) #待机面朝相机
playerLeftFrame = []
for frame in playerRightFrame:
    playerLeftFrame.append(pygame.transform.flip(frame, True, False))
playerHealth = pygame.image.load('./resouces/health.png')

# -----方块素材
blockImage = pygame.image.load('./resouces/terrain1.png')
stone = pygame.image.load('./resouces/blocks/stone.png')
soil = pygame.image.load('./resouces/blocks/dirt.png')
grass = pygame.image.load('./resouces/blocks/grass_side.png')
granite = pygame.image.load('./resouces/blocks/stonebrick_carved.png')
diamond_ore = ImageHandleTools.get_image(pygame.image.load('./resouces/blocks/diamond_ore.png'), 0, 0, 16, 16, pygame.Color(0, 0, 0))
coal_ore = ImageHandleTools.get_image(pygame.image.load('./resouces/blocks/coal_ore.png'), 0, 0, 16, 16, pygame.Color(0, 0, 0))
water = pygame.image.load('./resouces/water.bmp')
grass_block_snow = pygame.image.load('./resouces/blocks/grass_side_snowed.png')
bedrock = pygame.image.load('./resouces/blocks/bedrock.png')
log_oak = pygame.image.load('./resouces/blocks/log_oak.png')
leaves_oak = pygame.image.load('./resouces/blocks/leaves_oak.png')
iron_ore = ImageHandleTools.get_image(pygame.image.load('./resouces/blocks/iron_ore.png'), 0, 0, 16, 16, pygame.Color(0, 0, 0))
cobblestone = pygame.image.load('./resouces/blocks/cobblestone.png')
#破坏方块动画
destroyBlockFrame = []
for index in range(9):
    destroyBlockFrame.append(pygame.image.load('./resouces/blocks/destroy_stage_' + str(index) + '.png'))

# -----物品素材
coalitem = pygame.image.load('./resouces/items/coal.png')

# -----魔法素材
magic1Frame = []
magic1Index = range(17)
for index in reversed(magic1Index):
    magic1Frame.append(pygame.image.load('./resouces/magic1/magic1_0000 (' + str((index + 1)) + ').png'))
magic2Frame = []
for index in range(6):
    magic2Frame.append(pygame.image.load('./resouces/magic2/' + str(index) + '.png'))

# -----装饰素材
scene1 = pygame.image.load('./resouces/scene1.png')
armshouse = ImageHandleTools.get_image(scene1, 720, 69, 180, 299, pygame.Color(0, 255, 0))

# -----工具素材
armss = pygame.image.load('./resouces/tool/arms.png')
arms1 = ImageHandleTools.get_image(armss, 16, 82, 45, 12, pygame.Color(0, 0, 0))
woodpickaxe = pygame.image.load('./resouces/items/wood_pickaxe.png')
cyclonestaff = ImageHandleTools.get_image(armss, 230, 39, 54, 23, pygame.Color(0, 0, 0))

# -----怪物素材
monster1Image = pygame.image.load('./resouces/entity/monster1.png')
monster1LeftFrame = []
monster1LeftFrame.append(pygame.transform.rotate(ImageHandleTools.get_image(monster1Image, 8, 115, 90, 84, pygame.Color(0, 0, 0)), 90))
monster1LeftFrame.append(pygame.transform.rotate(ImageHandleTools.get_image(monster1Image, 8, 296, 90, 84, pygame.Color(0, 0, 0)), 90))
monster1RightFrame = []
for frame in monster1LeftFrame:
    monster1RightFrame.append(pygame.transform.flip(frame, True, False))
from pygame.math import *

'''
    计算一个坐标移动到另外一个坐标之间的每一帧移动的坐标数
'''
def movepos(startX, startY, endX, endY, speed):
    complete = False
    endPos = Vector2(endX, endY)   #结束的位置
    startPos = Vector2(startX, startY)   #设置初始位置
    dis = endPos - startPos
    dis_lenth = dis.length()  #计算物体到鼠标点击处的距离
    if dis_lenth < speed: #做一个判断，如果距离小于速度，则不需要移动
        endPos = startPos
        complete = True
    elif dis_lenth != 0:
        dis.normalize_ip()  #坐标归一化非常重要
        dis = dis * speed  #计算每一帧移动的坐标数
        startPos += dis  #叠加每次移动的坐标
    return startPos, complete

'''
    计算一个坐标移动到另外一个坐标之间的距离
'''
def poslen(startX, startY, endX, endY):
    endPos = Vector2(endX, endY)
    startPos = Vector2(startX, startY)
    dis = endPos - startPos
    dis_lenth = dis.length()
    return dis_lenth
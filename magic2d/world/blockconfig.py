from magic2d.world.block import *

def createBlock(blockID, x, y):
    newBlock = None
    if blockID == 0:
        Air = air.Air()
        Air.setLocation(30 * x, 30 * y)
        newBlock = Air
    if blockID == 1:
        Stone = stone.Stone()
        Stone.setLocation(30 * x, 30 * y)
        newBlock = Stone
    elif blockID == 2:
        Soil = soil.Soil()
        Soil.setLocation(30 * x, 30 * y)
        newBlock = Soil
    elif blockID == 3:
        Grass = grass.Grass()
        Grass.setLocation(30 * x, 30 * y)
        newBlock = Grass
    elif blockID == 4:
        Granite = granite.Granite()
        Granite.setLocation(30 * x, 30 * y)
        newBlock = Granite
    elif blockID == 5:
        Diamond_ore = diamond_ore.DiamondOre()
        Diamond_ore.setLocation(30 * x, 30 * y)
        newBlock = Diamond_ore
    elif blockID == 6:
        Water = water.Water()
        Water.setLocation(30 * x, 30 * y)
        newBlock = Water
    elif blockID == 7:
        GrassBlockSnow = grass_block_snow.GrassBlockSnow()
        GrassBlockSnow.setLocation(30 * x, 30 * y)
        newBlock = GrassBlockSnow
    elif blockID == 8:
        coalOre = coal_ore.CoalOre()
        coalOre.setLocation(30 * x, 30 * y)
        newBlock = coalOre
    elif blockID == 9:
        bedRock = bedrock.Bedrock()
        bedRock.setLocation(30 * x, 30 * y)
        newBlock = bedRock
    elif blockID == 10:
        logoak = log_oak.Logoak()
        logoak.setLocation(30 * x, 30 * y)
        newBlock = logoak
    elif blockID == 11:
        leavesoak = leaves_oak.Leavesoak()
        leavesoak.setLocation(30 * x, 30 * y)
        newBlock = leavesoak
    elif blockID == 12:
        ironore = iron_ore.IronOre()
        ironore.setLocation(30 * x, 30 * y)
        newBlock = ironore
    elif blockID == 13:
        cobbleStone = cobblestone.CobbleStone()
        cobbleStone.setLocation(30 * x, 30 * y)
        newBlock = cobbleStone
    return newBlock
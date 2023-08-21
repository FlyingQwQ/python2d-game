import pygame

def get_image(res:pygame.Surface, x, y, width, height, colorKey):
    image = pygame.Surface((width, height))
    image.blit(res, (0, 0), (x, y, width, height))
    image.set_colorkey(colorKey)
    # image.fill(pygame.Color(255, 0, 0))
    return image


def scale(surface:pygame.Surface, width, height):
    return pygame.transform.scale(surface, (width, height))

def widthScale(surface:pygame.Surface, width):
    rect = surface.get_rect()
    newWidth = int(width)
    newHeight = int((rect.height * width) / rect.width)
    return pygame.transform.scale(surface, (newWidth, newHeight))
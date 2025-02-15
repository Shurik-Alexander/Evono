import pygame

class texture:
    def texture(self, way, clear=None, size_x=None, size_y=None):
        if size_x == None: size_x = self.meter
        if size_y == None: size_y = self.meter
        texture = pygame.image.load(way)
        if clear != None: texture.set_colorkey(clear)
        texture = pygame.transform.scale(texture, (size_x, size_y))
        return texture
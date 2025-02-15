import pygame

class cache:
    
    text_save = dict()
    def text(text, color, size):
        if (text, color, size) in cache.text_save:
            return cache.text_save[(text, color, size)]
        else:
            font = pygame.font.Font(None, size)
            render = font.render(text, True, color)
            cache.text_save[(text, color, size)] = render
            return render
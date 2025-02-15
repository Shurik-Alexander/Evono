import pygame
import time

from core.window.interface.interface import interface
from core.window.render import render
from core.control.control import control

def window(physics_box):
    
    pygame.init()
    pygame.mixer.init()
    
    physics_box.screen = pygame.display.set_mode((physics_box.window.x, physics_box.window.y))
    clock = pygame.time.Clock()
    
    while physics_box.run:
        t3 = time.time()
        clock.tick(60)
        t4 = time.time()
        #print(t4-t3)
        
        t1 = time.time()
        
        physics_box.events = pygame.key.get_pressed()
        control(physics_box, pygame.event.get())
        
        pygame.display.set_caption(physics_box.window.name)
        #pygame.display.set_caption(str(int(clock.get_fps())))
        
        physics_box.screen.fill(physics_box.window.color)
        render(physics_box)
        
        try:
            interface(physics_box)
        except BaseException as error:
            if physics_box.error_log:
                open('errors.txt', 'a', encoding='utf-8').write(f'[interfase] {error}\n')
        
        pygame.display.flip()
        t2 = time.time()
        
        if physics_box.check_frame: print(f'Window   {t2 - t1 < 1 / 60}  {t2 - t1}')
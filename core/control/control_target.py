import pygame
import time

from core.control.movement import movement
from core.control.transfer import transfer

def control_target(physics_box):
    
    clock = pygame.time.Clock()
    while physics_box.run:
        clock.tick(60)
        t1 = time.time()
        
        movement(physics_box)
        transfer(physics_box)
    
        t2 = time.time()
        if physics_box.check_frame: print(f'Control  {t2 - t1 < 1 / 60}  {t2 - t1}')
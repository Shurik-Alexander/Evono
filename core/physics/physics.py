from core.api.api import core_class
from core.physics.friction import friction
import pygame

def physics(core:core_class):
    
    clock = pygame.time.Clock()
    while core.run:
        clock.tick(60)
        l = list(core.scene)
        for id in l:
            try:

                block = core.scene[id]
                if block.physical:
                    
                    if core.sticking(id) == False:
                    
                        if block.gravity:
                            block.speed_y += core.g
                        
                        if block.speed_x > core.speed_limit: block.speed_x = core.speed_limit
                        if block.speed_y > core.speed_limit: block.speed_y = core.speed_limit
                        if block.speed_x < -core.speed_limit: block.speed_x = -core.speed_limit
                        if block.speed_y < -core.speed_limit: block.speed_y = -core.speed_limit
                    
                        if block.speed_y > 0:
                            core.move_down(id, block.speed_y)
                    
                        if block.speed_y < 0:
                            core.move_up(id, -block.speed_y)
                    
                        if block.speed_x > 0:
                            core.move_right(id, block.speed_x)
                    
                        if block.speed_x < 0:
                            core.move_left(id, -block.speed_x)
                        
                        friction(core, id)
                
                if block.y > 10_000:
                    del core.scene[id]
        
            except BaseException as error: core.log_error(f'[physics] [{id}] {error}\n')
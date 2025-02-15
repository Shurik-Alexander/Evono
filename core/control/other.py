import pygame
from core.window.editor import editor

def other(physics_box, event):
    
    if event.type == pygame.KEYDOWN:
            
        if event.key == pygame.K_e:
            x = physics_box.mouse.x
            y = physics_box.mouse.y
            id = physics_box.get(x, y)
            if id != None:
                try:
                    physics_box.scene[id].poke()
                except BaseException as error:
                    physics_box.log_error(f'[screpts] [poke] [{id}] {error}\n')
            
        if event.key == pygame.K_q:
            x = physics_box.mouse.x
            y = physics_box.mouse.y
            if physics_box.get(x, y) != None:
                physics_box.item_in_hand = physics_box.scene[
                    physics_box.get(x, y)
                ]
        
        '''
        if event.key == pygame.K_x:
            x = physics_box.mouse.x
            y = physics_box.mouse.y
            id = physics_box.get(x, y)
            if id != None:
                #print(physics_box.scene[id].__script__)
                editor(physics_box, id)
        '''
            
        if event.key == pygame.K_TAB:
            if physics_box.building_mode:
                physics_box.building_mode = False
            else:
                physics_box.building_mode = True
            
        if event.key == pygame.K_p:
            if physics_box.pause:
                physics_box.pause = False
            else:
                physics_box.pause = True
            
        if event.key == pygame.K_F3:
            if physics_box.debug_menu:
                physics_box.debug_menu = False
            else:
                physics_box.debug_menu = True
import pygame

def mouse(physics_box, event):
        
        if event.type == pygame.MOUSEMOTION:
            x = event.pos[0] + physics_box.camera.x
            y = event.pos[1] + physics_box.camera.y
            physics_box.mouse.x = x
            physics_box.mouse.y = y
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            
            x = event.pos[0] + physics_box.camera.x
            y = event.pos[1] + physics_box.camera.y
            physics_box.mouse.x = x
            physics_box.mouse.y = y
            
            item_in_hand = physics_box.item_in_hand
            
            if event.button == 3:
                if item_in_hand.__type__ == 'block':
                    if physics_box.building_mode:
                        x = x // item_in_hand.size_x * item_in_hand.size_x
                        y = y // item_in_hand.size_y * item_in_hand.size_y
                    else:
                        x = x - item_in_hand.size_x / 2
                        y = y - item_in_hand.size_y / 2
                    physics_box.spawn(item_in_hand, x, y)
                if item_in_hand.__type__ == 'item':
                    item_in_hand.poke(x, y)
            
            if event.button == 1:
                try:
                    if item_in_hand.poke2 == None:
                        physics_box.despawn(
                            physics_box.get(x, y)
                        )
                    else:
                        item_in_hand.poke2(x, y)
                except BaseException as error:
                    physics_box.log_error(f'[screpts] [poke2] [{id}] {error}\n')
            
            if event.button == 2:
                try:
                    if item_in_hand.poke3 == None:
                        if physics_box.block_in_hand == None:
                            if physics_box.get(x, y) != None:
                                physics_box.block_in_hand = physics_box.get(x, y)
                        else:
                            physics_box.block_in_hand = None
                    else:
                        item_in_hand.poke3(x, y)
                except BaseException as error:
                    physics_box.log_error(f'[screpts] [poke3] [{id}] {error}\n')
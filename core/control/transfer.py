import pygame

def transfer(physics_box):
    
    block_in_hand = physics_box.block_in_hand
        
    if block_in_hand != None:
        if block_in_hand in physics_box.scene:
                
            block = physics_box.scene[block_in_hand]
                
            if physics_box.building_mode:
                x = physics_box.mouse.x // block.size_x * block.size_x
                y = physics_box.mouse.y // block.size_y * block.size_y
            else:
                x = physics_box.mouse.x - block.size_x / 2
                y = physics_box.mouse.y - block.size_y / 2
                
            physics_box.scene[block_in_hand].x = x
            physics_box.scene[block_in_hand].y = y
            physics_box.scene[block_in_hand].speed_x = 0
            physics_box.scene[block_in_hand].speed_y = 0
        else:
            physics_box.block_in_hand = None
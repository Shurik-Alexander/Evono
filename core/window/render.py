import pygame

def render(physics_box):
    
    camera_x = physics_box.camera.x
    camera_y = physics_box.camera.y
    
    l = list(physics_box.scene)
    for id in l:
        try:
            block = physics_box.scene[id]
            
            if block.texture == None:
                pygame.draw.rect(
                    physics_box.screen, block.color_1, 
                    (
                        block.x - camera_x, block.y - camera_y,
                        block.size_x, block.size_y
                    )
                )
        
                pygame.draw.rect(
                    physics_box.screen, block.color_2, 
                    (
                        block.x - camera_x, block.y - camera_y,
                        block.size_x, block.size_y
                    ),4
                )
    
            else:
                physics_box.screen.blit(block.texture, (block.x - camera_x, block.y - camera_y,))
        
        except BaseException as error: physics_box.log_error(f'[render] [{id}] {error}\n')
import pygame

def window(physics_box, event):
        
        if event.type == pygame.QUIT:
            physics_box.run = False
        
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_ESCAPE:
                physics_box.run = False
        
            if event.key == pygame.K_F11:
                if physics_box.window.full:
                    physics_box.window.full = False
                    pygame.display.set_mode((physics_box.window.x, physics_box.window.y))
                else:
                    physics_box.window.full = True
                    pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
import pygame

def movement(physics_box):
    
    events = physics_box.events
    
    if len(events) != 0:

        if events[pygame.K_LSHIFT]:
            speed = physics_box.camera.fast_speed
        
        elif events[pygame.K_LCTRL]:
            speed = physics_box.camera.slow_speed
        
        else:
            speed = physics_box.camera.speed

        if events[pygame.K_w]:
            physics_box.camera.y -= speed
            physics_box.mouse.y -= speed
            
        if events[pygame.K_a]:
            physics_box.camera.x -= speed
            physics_box.mouse.x -= speed
    
        if events[pygame.K_s]:
            physics_box.camera.y += speed
            physics_box.mouse.y += speed
    
        if events[pygame.K_d]:
            physics_box.camera.x += speed
            physics_box.mouse.x += speed
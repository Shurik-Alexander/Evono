import pygame

def inventory(physics_box, event):
        
        if event.type == pygame.KEYDOWN:
        
            item_in_hand = physics_box.item_in_hand
            hotbar = physics_box.hotbar
        
            if event.key == pygame.K_LEFT:
                if item_in_hand in hotbar:
                    index = hotbar.index(item_in_hand)
                    if index == len(hotbar)-1:
                        physics_box.item_in_hand = hotbar[0]
                    else:
                        physics_box.item_in_hand = hotbar[index+1]
                else: 
                    physics_box.item_in_hand = hotbar[0]

            if event.key == pygame.K_RIGHT:
                if item_in_hand in hotbar:
                    index = hotbar.index(item_in_hand)
                    if index == 0:
                        physics_box.item_in_hand = hotbar[len(hotbar)-1]
                    else:
                        physics_box.item_in_hand = hotbar[index-1]
                else: 
                    physics_box.item_in_hand = hotbar[0]
        
        if event.type == pygame.MOUSEBUTTONDOWN:
        
            item_in_hand = physics_box.item_in_hand
            hotbar = physics_box.hotbar
        
            if event.button == 6:
                if item_in_hand in hotbar:
                    index = hotbar.index(item_in_hand)
                    if index == len(hotbar)-1:
                        physics_box.item_in_hand = hotbar[0]
                    else:
                        physics_box.item_in_hand = hotbar[index+1]
                else: 
                    physics_box.item_in_hand = hotbar[0]

            if event.button == 7:
                if item_in_hand in hotbar:
                    index = hotbar.index(item_in_hand)
                    if index == 0:
                        physics_box.item_in_hand = hotbar[len(hotbar)-1]
                    else:
                        physics_box.item_in_hand = hotbar[index-1]
                else: 
                    physics_box.item_in_hand = hotbar[0]
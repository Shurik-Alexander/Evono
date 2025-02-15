from core.api.api import core_class

def frame(physics_box:core_class):
    try:
        if physics_box.building_mode:
            if physics_box.block_in_hand == None:
                if physics_box.item_in_hand.__type__ == 'block':
                    if physics_box.item_in_hand.size_x == physics_box.meter:
                        if physics_box.item_in_hand.size_x == physics_box.meter:
                            physics_box.screen.blit(
                                physics_box.frame,
                                (
                                    (physics_box.mouse.x - physics_box.camera.x) - physics_box.mouse.x % physics_box.meter,
                                    (physics_box.mouse.y - physics_box.camera.y) - physics_box.mouse.y % physics_box.meter
                                )
                            )
    except: pass
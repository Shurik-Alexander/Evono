from core.window.interface.text import *
from core.window.interface.debug import *

text = text()

def interface(physics_box):
    
    text.core = physics_box

    text.add(physics_box.item_in_hand.name, physics_box.item_in_hand.name_color)
    
    if physics_box.building_mode:
        text.add('Строительный режим')
    
    if physics_box.debug_menu:
        debug(physics_box, text)
    
    text.clear()
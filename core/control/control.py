from core.control.inventory import inventory
from core.control.mouse import mouse
from core.control.window import window
from core.control.other import other

def control(physics_box, events):
    for event in events:
        inventory(physics_box, event)
        mouse(physics_box, event)
        window(physics_box, event)
        other(physics_box, event)
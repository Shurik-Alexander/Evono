from core.api.api import core

class not_gravity(core.block):
    surname = 'not gravity'
    name = 'Ливитирующий блок'
    color_1 = (230, 230, 230)
    color_2 = (0, 255, 255)
    gravity = False

core.addscript(not_gravity)
#physics_box.inventory.hotbar.append(not_gravity)

from core.api.api import core_class

def friction(core: core_class, id):
    block = core.scene[id]
    
    if block.speed_x > 0:
        if len(core.touch_down(id)) > 0:
            if block.speed_x > core.friction:
                core.scene[id].speed_x -= core.friction
            else:
                core.scene[id].speed_x = 0
    
    if block.speed_x < 0:
        if len(core.touch_down(id)) > 0:
            if block.speed_x < core.friction:
                core.scene[id].speed_x += core.friction
            else:
                core.scene[id].speed_x = 0
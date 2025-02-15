from core.api.api import *

class gravity_tool(core.item):
    from content.not_gravity import not_gravity

    def poke(self, x, y):
        id = core.get(x, y)
        if id != None:
            
            a = True
            if core.scene[id].surname == 'white block':
                l = core.touch_down(id)
                for a in l:
                    if core.scene[a].surname == 'table':
                        Bx = core.scene[id].x
                        By = core.scene[id].y
                        core.despawn(id)
                        core.spawn(self.not_gravity, Bx, By, id=id)
                        a = False
            
            if a:
                gravity = core.scene[id].gravity
                if gravity:
                    core.scene[id].gravity = False
                else:
                    core.scene[id].gravity = True
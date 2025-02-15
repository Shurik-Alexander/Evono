from core.api.api import core

class brush(core.item):
    from content.dye import dye
    name = 'Кисточка'
    
    color_1 = (230, 230, 230)
    color_2 = (200, 200, 200)
    index = 0
    colors = [
        (230, 230, 230),
        (230, 0, 0),
        (0, 230, 0),
        (0, 0, 230),
        (230, 200, 0),
        (230, 100, 0),
        (230, 0, 230),
        (40, 40, 40)
    ]

    def poke(self, x, y):

        id = core.get(x, y)
        
        if id == None:
            if self.index == None: self.index = 0
            elif self.index == len(self.colors) - 1: self.index = 0
            else: self.index += 1
            self.color_1 = self.colors[self.index]
            r = self.color_1[0] - 30
            g = self.color_1[1] - 30
            b = self.color_1[2] - 30
            if r < 0: r = 0
            if g < 0: g = 0
            if b < 0: b = 0
            self.color_2 = (r, g, b)
            self.name_color = self.color_1
        
        else:
            
            if core.scene[id].surname == 'white block':
                l = core.touch_down(id)
                for a in l:
                    if core.scene[a].surname == 'table':
                        Bx = core.scene[id].x
                        By = core.scene[id].y
                        core.despawn(id)
                        core.spawn(self.dye, Bx, By, id=id)

            core.scene[id].color_1 = self.color_1
            core.scene[id].color_2 = self.color_2
            core.scene[id].name_color = self.color_2
            
    def poke2(self, x, y):
        id = core.get(x, y)
        if id != None:
            block = core.scene[id]
            self.color_1 = block.color_1
            self.color_2 = block.color_2
            self.index = None
            self.name_color = self.color_1

core.addscript(brush)
from core.api.api import core

class sapling(core.block):
    
    surname = 'sapling'
    name = 'Дерево'
    sticky = False
    texture = core.texture('asets/sapling.png')
    
    class leaves(core.block):
        surname = 'leaves'
        name = 'Листья'
        color_1 = (0, 200, 0)
        color_2 = (0, 170, 0)
        def poke(self):
            l = core.touch_down(self.id)
            for a in l:
                if core.scene[a].surname == 'table':
                    core.despawn(self.id)
                    core.spawn(sapling, self.x, self.y, id=id)

    class log(core.block):
        surname = 'log'
        name = 'Бревно'
        color_1 = (140, 96, 39)
        color_2 = (110, 66, 9)

    def poke(self):
        
        x = self.x
        y = self.y
        
        for b in range(3):
            core.spawn(self.log, x, y - b * core.meter)
        
        for a in range(-2, 3):
            for b in range(3, 5):
                core.spawn(self.leaves, x + a * core.meter, y - b * core.meter)
        
        for a in range(-1, 2):
            for b in range(5, 7):
                core.spawn(self.leaves, x + a * core.meter, y - b * core.meter)
        
        core.spawn(self.leaves, x, y - 7 * core.meter)
        core.despawn(self.id)

core.addscript(sapling)
core.addscript(sapling.log)
core.addscript(sapling.leaves)
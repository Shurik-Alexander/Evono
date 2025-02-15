from core.api.api import core

class tower(core.item):
    
    name = 'Башня'

    def poke(self, x, y):
        from content.TNT import TNT
        
        x = x // core.meter * core.meter
        y = y // core.meter * core.meter
        
        for b in range(7):
            core.spawn(core.block(), x - 2 * core.meter, y - b * core.meter)
        
        for b in range(7):
            core.spawn(core.block(), x + 2 * core.meter, y - b * core.meter)
        
        for a in range(-1, 2):
            core.spawn(core.block(), x + a * core.meter, y - 3 * core.meter)
        
        for a in range(-3, 4):
            core.spawn(core.block(), x + a * core.meter, y - 7 * core.meter)
        
        for a in range(-3, 4):
            if a % 2 != 0:
                core.spawn(core.block(), x + a * core.meter, y - 8 * core.meter)
        
        core.spawn(TNT, x + 0 * core.meter, y - 4 * core.meter)
        
from core.api.api import core

class pc(core.block):
    surname = 'pc'
    name = 'Компъютер'
    sticky = False

    texture_f1 = core.texture('asets/pc/f1.bmp', clear=(200, 200, 200))
    texture_f2 = core.texture('asets/pc/f2.bmp', clear=(200, 200, 200))
    texture_t1 = core.texture('asets/pc/t1.bmp', clear=(200, 200, 200))
    texture_t2 = core.texture('asets/pc/t2.bmp', clear=(200, 200, 200))

    texture_1 = texture_f1
    texture_2 = texture_f2

    texture = texture_1

    def check(self):
        
        '''
        id = core.get(self.x+32, self.y+32+64)
        if id == None:
            return False
        if core.scene[id].surname != 'table':
            return False
        
        id = core.get(self.x+32+64, self.y+32+64)
        if id == None:
            return False
        if core.scene[id].surname != 'table':
            return False
        '''
        
        id = core.get(self.x+32+64, self.y+32)
        if id == None:
            return False
        
        return True
    
    time = 0
    frame = 1

    def tick(self):

        if self.check():
            self.texture_1 = self.texture_t1
            self.texture_2 = self.texture_t2
        else:
            self.texture_1 = self.texture_f1
            self.texture_2 = self.texture_f2

        if self.time == 15:
            if self.frame > 0:
                self.texture = self.texture_2
            else:
                self.texture = self.texture_1
            self.frame *= -1
            self.time = 0
        
        self.time += 1
    
    def poke(self):
        if self.check():
            id = core.get(self.x+32+64, self.y+32)
            core.edit(id)
        
core.addscript(pc)
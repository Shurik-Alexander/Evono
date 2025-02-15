from core.api.api import core

class TNT(core.block):
    name = 'Бочка с динамитом'
    surname = 'TNT'
    texture = core.texture('asets/TNT.bmp', clear=(255, 255, 255))
    boom_sound = core.sound('asets/sounds/boom.ogg')
    sticky = False

    def poke(self):
        core.despawn(self.id)
        core.boom(self.x, self.y, 500, 30)
        self.boom_sound.play()
    
    def boom(self):
        core.despawn(self.id)
        core.boom(self.x, self.y, 500, 30)
        self.boom_sound.play()

core.addscript(TNT)
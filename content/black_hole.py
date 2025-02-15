from core.api.api import core

class black_hole(core.block):
    from random import randint as r

    surname = 'black hole'
    name = 'Чёрная дыра'
    color_1 = (0, 0, 0)
    color_2 = (0, 0, 0)
    physical = False
    sound = core.sound('asets/sounds/black hole.mp3')
    sound_clock = 0
    
    def spawn(self):
        self.sound.play()
        core.window.color = (110, 169, 235)

    def tick(self):

        if self.r(0, 1): core.camera.x += self.r(-1, 1)
        else: core.camera.y += self.r(-1, 1)
        
        core.boom(self.x, self.y, 1500, -10)
        
        for id in core.touch(self.id):
            del core.scene[id]
        
        if self.sound_clock == 100:
            self.sound.play()
            self.sound_clock = 0
        
        self.sound_clock += 1
    
    def despawn(self):
        if len(core.search('black hole')) == 1:
            core.window.color = (127, 199, 255)
            self.sound.stop()

core.addscript(black_hole)
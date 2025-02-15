from core.api.api import core

class dye(core.block):
    name = 'Краситель'
    surname = 'dye'
    gravity = False
    sound = core.sound('asets/sounds/.mp3')

    def tick(self):
        self.name_color = self.color_1
        for id in core.touch(self.id):
            if core.scene[id].color_1 != self.color_1:
                if core.scene[id].color_2 != self.color_2:
                    core.scene[id].color_1 = self.color_1
                    core.scene[id].color_2 = self.color_2
                    self.sound.play()

core.addscript(dye)
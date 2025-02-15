from core.api.api import core

class box(core.block):
    name = 'Каробка'
    surname = 'box'
    texture = core.texture('asets/box.bmp', clear=(255, 255, 255))
    sticky = False
    content = None
    sound1 = core.sound('asets/sounds/box1.mp3')
    sound2 = core.sound('asets/sounds/box2.mp3')

    def despawn(self):
        if self.content != None:
            core.spawn(self.content, self.x, self.y - self.content.size_y + core.meter)
            self.sound2.play()
    
    def tick(self):
        if self.content == None:
            id = core.touch_up(self.id)[0]
            if id != None and id != self.id:
                self.content = core.scene[id]
                core.despawn(id)
                self.sound1.play()

core.addscript(box)
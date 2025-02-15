from core.api.api import core

class exterminator(core.block):
    from content.black_hole import black_hole

    surname = 'exterminator'
    name = 'Уничтожитель'
    color_1 = (0, 0, 0)
    color_2 = (230, 0, 0)
    gravity = False
    sound = core.sound('asets/sounds/.mp3')
    
    def tick(self):
        for id in core.touch(self.id):
            if id != self.id and core.scene[id].surname != 'black hole':
                if core.scene[id].surname == 'exterminator':
                    core.despawn(id)
                    core.despawn(self.id)
                    core.spawn(self.black_hole, self.x, self.y)
                else:
                    core.despawn(id) 
                    self.sound.play()

core.addscript(exterminator)
#physics_box.inventory.hotbar.append(exterminator)
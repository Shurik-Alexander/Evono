from core.api.api import core

def void(self): pass

class chisel(core.item):
    name = 'Стамеска'
    def poke(self, x, y):
        id = core.get(x, y)
        if id != None:
            block = core.scene[id]
            if block.size_x == 64:
                if block.size_y == 64:
                    if block.texture == None:
                        x = block.x
                        y = block.y
                        class MiniBlock(core.block):
                            name = block.name
                            surname = 'MiniBlock'
                            name_color = block.name_color
                            color_1 = block.color_1
                            color_2 = block.color_2
                            physical = block.physical
                            gravity = block.gravity
                            sticky = block.sticky
                            size_x = 32
                            size_y = 32
                        core.addscript(MiniBlock)
                        core.scene.pop(id)
                        core.spawn(MiniBlock, x, y)
                        core.spawn(MiniBlock, x+32, y)
                        core.spawn(MiniBlock, x, y+32)
                        core.spawn(MiniBlock, x+32, y+32)
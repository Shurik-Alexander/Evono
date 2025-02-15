from core.api.api import core

class table(core.block):
    name = 'Стол'
    surname = 'table'
    texture = core.texture('asets/table.bmp', (255, 255, 255))
    sticky = False

core.addscript(table)
from core.api.api import *

class not_physical(core.block):
    name = 'Не физический блок'
    surname = 'not physical'
    color_1 = (210, 210, 210)
    color_2 = (180, 180, 180)
    physical = False

core.addscript(not_physical)
from scene import *

content = '''
from content.not_physical import *
from content.not_gravity import *
from content.gravity_tool import *
from content.TNT import *
from content.exterminator import *
from content.brush import *
from content.dye import *
from content.box import *
from content.black_hole import *
from content.chisel import *
from content.table import *
from content.pc import *
'''

for line in content.split('\n'):
    exec(line)

core.give(box)
core.give(exterminator)
core.give(gravity_tool)
core.give(chisel)
core.give(brush)
core.give(table)
core.give(TNT)
core.give(not_physical)
core.give(pc)
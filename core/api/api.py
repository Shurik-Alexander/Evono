import dataclasses

from core.api.scene.scene import scene
from core.api.block import block
from core.api.item import item
from core.api.texture import texture
from core.api.sound import sound
from core.api.give import give
from core.api.addscript import addscript
from core.api.search import search
from core.physics.api import ph_api
from core.window.editor import editor

@dataclasses.dataclass()
class core_class(ph_api, scene, block, item, texture, sound, give, addscript, search):

    run = True
    meter = 64
    events = list()
    
    building_mode = False
    pause = False
    check_frame = False
    debug_menu = False
    
    hotbar = [block.block()]
    item_in_hand = block.block()
    block_in_hand = None
    
    class window:
        name = 'Сode Sandbox'
        color = (127, 199, 255)
        x = 1500
        y = 750
        full = False
    
    class camera:
        x = 0
        y = -750 + 64
        speed = 10
        fast_speed = 20
        slow_speed = 3
    
    class mouse:
        x = int()
        y = int()
    
    error_log = False
    def log_error(self, promt):
        if self.error_log:
            open('errors.txt', 'a', encoding='utf-8').write(promt)
    
    edit = editor

core = core_class()
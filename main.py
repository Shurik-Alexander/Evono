import time
load_1 = time.time()

import threading
import pygame
pygame.mixer.init()

from core.api.api import *

core.frame = core.texture('asets/frame.bmp', clear=(255, 255, 255))

from core.window.window import *
from core.physics.physics import *
from core.control.control_target import *
from core.cmd import *

from load_content import *

threading.Thread(target=window, args=(core,)).start()
threading.Thread(target=control_target, args=(core,)).start()
threading.Thread(target=physics, args=(core,)).start()

load_2 = time.time()

print(f'Загрузка заняла {load_2 - load_1} секунд.')
print(open('hello.txt', encoding='utf-8').read())
#threading.Thread(target=cmd, args=(core,)).start()

clock = pygame.time.Clock()
while core.run:
    clock.tick(20)
    if core.pause == False:
        l = list(core.scene)
        for id in l:
            try:
                core.scene[id].tick()
            except BaseException as error:
                core.log_error(f'[screpts] [tick] [{id}] {error}\n')
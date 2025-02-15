from core.physics.api import ph_block

class block:
    class block(ph_block):
        
        name = 'Блок'
        surname = 'white block'
        name_color = (230, 230, 230)
        color_1 = (230, 230, 230)
        color_2 = (200, 200, 200)
        size_x = 64
        size_y = 64
        texture = None
        x = int()
        y = int()
        id = None
        def poke(self): pass # взаимодействие
        def spawn(self): pass # установка
        def tick(self): pass # постоянно
        def despawn(self): pass # сломан
        def boom(self): pass # падован
        poke2 = None
        poke3 = None
        
        __script__ = str()
        __type__ = 'block'
        __initing__ = False
        def __init__(self): self.__initing__ = True
        def new(self): return self
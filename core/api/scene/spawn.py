import inspect
from random import randint as r

class spawn:
    def spawn(self, block, x, y, id=None, speed_x=0, speed_y=0):
        
        if block.__initing__ == False: block = block()
        
        if id == None:
            id = 0
            run = True
            while run:
                if id in self.scene:
                    id += 1
                else:
                    run = False
        
        args = vars(block)
        class block(type(block)): pass
        for arg in args:
            val = args[arg]
            exec(f'block.{arg} = val')
        
        args = dir(block)
        for arg in args:
            if type(arg) == type(print):
                arg = eval(f'block.{arg}')
                arg = inspect.getsource(arg)
                exec(arg)
                exec(f'block.{arg} = {arg}')

        block.x = x
        block.y = y
        block.speed_x = speed_x
        block.speed_y = speed_y
        block.id = id

        self.scene[id] = block()
        
        try:
            self.scene[id].spawn()
        except BaseException as error:
                self.log_error(f'[screpts] [spawn] [{id}] {error}\n')

        return id
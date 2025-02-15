from core.api.block import block

class structure:
    
    class structure:
        name = 'Башня'
        blocks = {'█': block}
        canvas = 'x'
        center = None

    def create_structure(self, structure:structure):
        
        canvas = structure.canvas.split('\n')
        tile = dict()
        y = 0
        for line in canvas:
            x = 0
            for symbol in canvas[x]:
                if symbol == 'x':
                    center = (x, y)
                else:
                    tile[(x, y)] = structure.blocks[symbol]
                x += 1
            y += 1
        
        fun = str()
        fun += 'def structure(x, y):' + '\n'
        for cord in tile:
            pass
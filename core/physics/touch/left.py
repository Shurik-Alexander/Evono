def left(self, id):
    
    am = self.scene[id]
    touch = set()

    l = list(self.scene)
    for id in l:
        block = self.scene[id]
        
        line = block.x + block.size_x
        if line < am.x + am.size_x:
            if line > am.x - 1:

                y = block.y + 1
                if (y >= am.y) and (y <= am.y + am.size_y):
                    touch.add(id)
                
                y = block.y + block.size_y - 1
                if (y >= am.y) and (y <= am.y + am.size_y):
                    touch.add(id)
    
    return list(touch)
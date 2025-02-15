def up(self, id):
    
    am = self.scene[id]
    touch = set()

    l = list(self.scene)
    for id in l:
        block = self.scene[id]
        
        line = block.y + block.size_y
        if line < am.y + am.size_y:
            if line > am.y - 1:

                x = block.x + 1
                if (x >= am.x) and (x <= am.x + am.size_x):
                    touch.add(id)
                
                x = block.x + block.size_x - 1
                if (x >= am.x) and (x <= am.x + am.size_x):
                    touch.add(id)
    
    return list(touch)
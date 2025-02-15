class get:
    def get(self, x, y, floor=True):
        
        l = list(self.scene)
        for id in l:
            block = self.scene[id]
            
            x1 = block.x
            x2 = block.x + block.size_x
            y1 = block.y
            y2 = block.y + block.size_y
            
            if x >= x1 and x <= x2:
                if y >= y1 and y <= y2:
                    return id
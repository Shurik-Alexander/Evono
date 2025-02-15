def up(self, id, distance):
    
    c = 1_000_000
    
    block = self.scene[id]
    
    y = block.y
    x1 = block.x + 0.01
    x2 = block.x + block.size_x - 0.01
    
    a = self.ray_up(x1, y)
    b = self.ray_up(x2, y)
    
    if a != None:
        if a < c:
            c = a
    if b != None:
        if b < c:
            c = b

    if c >= distance:
        block.y -= distance
    else:
        block.y -= c
        block.speed_y = 0
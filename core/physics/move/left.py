def left(self, id, distance):
    
    c = 1_000_000
    
    block = self.scene[id]
    
    x = block.x
    y1 = block.y + 0.01
    y2 = block.y + block.size_y - 0.01
    
    a = self.ray_left(x, y1)
    b = self.ray_left(x, y2)
    
    if a != None:
        if a < c:
            c = a
    if b != None:
        if b < c:
            c = b

    if c >= distance:
        block.x -= distance
    else:
        block.x -= c
        block.speed_x = 0
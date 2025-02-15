def right(self, id, distance):

    c = 1_000_000
    
    block = self.scene[id]
    
    x = block.x + block.size_x
    y1 = block.y + 0.01
    y2 = block.y + block.size_y - 0.01
    
    if x > 0: x += 0.01
    
    a = self.ray_right(x, y1)
    b = self.ray_right(x, y2)
    
    if a != None:
        if a < c:
            c = a
    if b != None:
        if b < c:
            c = b

    if c >= distance:
        block.x += distance
    else:
        block.x += c
        block.speed_x = 0
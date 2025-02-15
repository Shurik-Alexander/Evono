def down(self, id, distance):
    
    c = 1_000_000
    
    block = self.scene[id]
    
    y = block.y + block.size_y
    x1 = block.x + 0.01
    x2 = block.x + block.size_x - 0.01
    
    if y > 0: y += 0.01
    
    a = self.ray_down(x1, y)
    b = self.ray_down(x2, y)
    
    if a != None:
        if a < c:
            c = a
    if b != None:
        if b < c:
            c = b

    if c >= distance:
        block.y += distance
    else:
        block.y += c
        block.speed_y = 0
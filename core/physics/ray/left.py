def left(self, x, y):
    m = 1_000_000
    l = list(self.scene)
    for id in l:
        block = self.scene[id]
        if block.x < x:
            if y >= block.y:
                if y <= block.y + block.size_y:
                    if x - block.x - block.size_x < m:
                        m = x - block.x - block.size_x
    if m == 1_000_000: return None
    return m
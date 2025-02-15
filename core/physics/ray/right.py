def right(self, x, y):
    m = 1_000_000
    l = list(self.scene)
    for id in l:
        block = self.scene[id]
        if block.x > x - block.size_x:
            if y >= block.y:
                if y <= block.y + block.size_y:
                    if block.x - x < m:
                        m = block.x - x
    if m == 1_000_000: return None
    return m
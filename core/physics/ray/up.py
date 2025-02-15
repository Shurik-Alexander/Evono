def up(self, x, y):
    m = 1_000_000
    l = list(self.scene)
    for id in l:
        block = self.scene[id]
        if block.y < y:
            if x >= block.x:
                if x <= block.x + block.size_x:
                    if y - int(block.y + block.size_y) < m:
                        m = y - block.y - block.size_y
    if m == 1_000_000: return None
    return m
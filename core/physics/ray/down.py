def down(self, x, y):
    m = 1_000_000
    l = list(self.scene)
    for id in l:
        block = self.scene[id]
        if block.y > y - block.size_y:
            if x >= block.x:
                if x <= block.x + block.size_x:
                    if block.y - y < m:
                        m = block.y - y
    if m == 1_000_000: return None
    return m
class boom:
    def boom(self, x, y, r, a):
        
        l = list(self.scene)
        for id in l:
            try:
                block = self.scene[id]
                if ((block.x - x)**2 + (block.y - y)**2)**0.5 <= r:
                    vector = [block.x - x, block.y - y]
                    vector_module = list()
                    vector_module.append(vector[0])
                    vector_module.append(vector[1])
                    if vector_module[0] < 0: vector_module[0] *= -1
                    if vector_module[1] < 0: vector_module[1] *= -1
                    if vector_module[0] + vector_module[1] != 0:
                        ax = (vector[0] / (vector_module[0] + vector_module[1])) * a
                        ay = (vector[1] / (vector_module[0] + vector_module[1])) * a
                        self.scene[id].speed_x += ax
                        self.scene[id].speed_y += ay
                        self.scene[id].boom()
                        
            except BaseException as error:
                self.log_error(f'[boom] [{id}] {error}\n')
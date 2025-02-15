class search:
    def search(self, surname):
        count = list()
        for id in self.scene:
            if surname == self.scene[id].surname:
                count += [id]
        return count
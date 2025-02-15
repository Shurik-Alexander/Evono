class give:
    def give(self, item):
        if item.__initing__ == False: item = item()
        self.hotbar.append(item)
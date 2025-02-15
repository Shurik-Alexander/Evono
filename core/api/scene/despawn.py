class despawn:
    def despawn(self, id):
        if id in self.scene:
            try:
                self.scene[id].despawn()
            except BaseException as error:
                self.log_error(f'[screpts] [despawn] [{id}] {error}\n')
            self.scene.pop(id)
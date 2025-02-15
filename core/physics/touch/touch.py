from core.physics.touch.up import up
from core.physics.touch.down import down
from core.physics.touch.right import right
from core.physics.touch.left import left

class touch:
    touch_up = up
    touch_down = down
    touch_right = right
    touch_left = left
    def touch(self, id):
        l = list()
        l += up(self, id)
        l += down(self, id)
        l += right(self, id)
        l += left(self, id)
        return l
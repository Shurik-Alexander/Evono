from core.physics.ray.ray import ray
from core.physics.touch.touch import touch
from core.physics.move.move import move
from core.physics.sticking import sticking
from core.physics.boom import boom

class ph_block:
    physical = True
    gravity = True
    sticky = True
    speed_x = int()
    speed_y = int()

class ph_api(ray, touch, move, sticking, boom):
    g = 0.5
    friction = 0.9
    speed_limit = 200
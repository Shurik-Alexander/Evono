from core.api.api import core_class
from core.cache import *

class text:

    отступ = 25
    counter = 0
    core = None

    def add(self, promt, color=(230, 230, 230)):

        x, y = 10, 10 + self.отступ * self.counter
        self.counter += 1

        text = cache.text(str(promt), color, 36)
        self.core.screen.blit(text, (x, y))

    def clear(self):
        self.counter = 0
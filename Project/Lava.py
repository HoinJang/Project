from pico2d import *

class Lava:
    image = None
    def __init__(self,sety):
            self.x = 400
            self.y = -300
            self.sety = sety
            self.image = load_image('Resource/Lava.png')
    def draw(self):
        self.image.draw(self.x, self.y+self.sety)
    def update(self):
        self.sety += 0.1
        pass
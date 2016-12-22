from pico2d import *

class Lava:
    image = None
    def __init__(self,sety):
            self.x = 400
            self.y = -300
            self.sety = sety
            self.image = load_image('Resource/Lava.png')
            self.timer = 0
    def draw(self):
        self.image.draw(self.x + self.timer, self.y+self.sety)
        self.image.draw(self.x-800 + self.timer, self.y+self.sety)
    def update(self):
        self.timer +=1
        self.sety += 0.1
        if self.x + self.timer == 1200:
            self.timer = 0
        pass
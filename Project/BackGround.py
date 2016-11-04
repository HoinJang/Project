from pico2d import *

class BackGround:
    image = None
    def __init__(self):
        self.x1 = 400
        self.x2 = 1200
        if BackGround.image == None:
            BackGround.image = load_image('Resource/BackGround.png')
    def update(self):
        self.x1 -= 1
        self.x2 -= 1
        if self.x1 == -400:
            self.x1 = 1200
        if self.x2 == -400:
            self.x2 = 1200
    def draw(self):
        self.image.draw(self.x1,300)
        self.image.draw(self.x2,300)
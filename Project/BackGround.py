from pico2d import *

class BackGround:
    image = None
    def __init__(self):
        self.x = 400
        self.y = 300
        if BackGround.image == None:
            BackGround.image = load_image('Resource/BackGround.png')
    def draw(self):
        self.image.draw(self.x, self.y)
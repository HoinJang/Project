from pico2d import *

class BackGround:
    image = None
    def __init__(self,stage):
            self.x = 400
            self.y = 300
            if stage == 1:
                if BackGround.image == None:
                    BackGround.image = load_image("Resource/BackGround/BackGround1.png")
            if stage == 2:
                    BackGround.image = load_image("Resource/BackGround/BackGround2.png")
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        self.image.draw(self.x, self.y)

from pico2d import *

class BackGround:
    image = None
    def __init__(self,stage):
            self.x = 400
            self.y = 300
            if stage == 1:
                if BackGround.image == None:
                    BackGround.image = load_image("Resource/BackGround/BackGround1.png")
            elif stage == 2:
                    BackGround.image = load_image("Resource/BackGround/BackGround2.png")
            elif stage == 3:
                    BackGround.image = load_image("Resource/BackGround/BackGround3.png")
            elif stage == 4:
                    BackGround.image = load_image("Resource/BackGround/BackGround4.png")
            elif stage == 5:
                    BackGround.image = load_image("Resource/BackGround/BackGround5.png")

    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        pass

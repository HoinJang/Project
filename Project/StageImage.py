from pico2d import *

class StageImage:
    image = None
    def __init__(self,stage):
            self.x = 400
            self.y = 300
            self.time =1
            if stage == 1:
                    StageImage.image = load_image("Resource/BackGround/Stage1.png")
            elif stage == 2:
                    StageImage.image = load_image("Resource/BackGround/Stage2.png")
            elif stage == 3:
                    StageImage.image = load_image("Resource/BackGround/Stage3.png")
            elif stage == 4:
                    StageImage.image = load_image("Resource/BackGround/Stage4.png")
            elif stage == 5:
                    StageImage.image = load_image("Resource/BackGround/Stage5.png")
    def draw(self):
        self.image.draw(self.x, self.y)
    def update(self):
        if self.time < 100:
            self.time +=1
        if self.time == 100:
            if(self.x < 1200):
                self.x += 10

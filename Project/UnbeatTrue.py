from pico2d import *

class UnbeatTrue:
    image = None
    def __init__(self,on,x,y):
            self.x = x
            self.y = y
            self.bool = on
            if UnbeatTrue.image == None:
                UnbeatTrue.image = load_image("Resource/Unbeat.png")
    def draw(self):
        if self.bool == True:
            self.image.draw(self.x, self.y)
    def update(self):
        pass

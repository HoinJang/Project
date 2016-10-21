from pico2d import *

class Barrel:
    image = None
    def __init__(self):
        self.frame = 0
        self.x = 80
        self.y = 455
        self.dx = 5
        self.dy = 5
        if Barrel.image == None :
            Barrel.image = load_image('Resource/Barrel.png')
    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 30, self.x, self.y)
    def update(self):
        self.frame +=1
        if self.y == 455:
            self.x += self.dx
        elif self.y == 325:
            self.x -= self.dx
        elif self.y == 195:
            self.x += self.dx
        elif self.y == 65:
            self.x -= self.dx

        if self.x >= 750:
            self.y -= self.dy
        if self.x <= 30:
            self.y -= self.dy
        if(self.frame > 7):
            self.frame = 0
    def __del__(self):
        if self.x < 30 and self.y < 65:
            del(Barrel)
import Macro
from pico2d import *

class Barrel:
    image = None
    def __init__(self):
        self.frame = 0
        self.x = 80
        self.y = 515
        self.dx = 5
        self.dy = 5
        if Barrel.image == None :
            Barrel.image = load_image('Resource/Barrel.png')
    def update(self):
        self.frame +=1
        if self.y == 515:
            self.x += self.dx
        elif self.y == 365:
            self.x -= self.dx
        elif self.y == 215:
            self.x += self.dx
        elif self.y == 65:
            self.x -= self.dx
        if self.x >= 750:
            self.y -= self.dy
        if self.x <= 30:
            self.y -= self.dy
        if(self.frame > 7):
            self.frame = 0
    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 30, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - Macro.barrel_size/ 2 + 5, self.y - Macro.barrel_size/ 2 + 5, self.x +Macro.barrel_size/ 2 -5 , self.y + Macro.barrel_size / 2 - 5
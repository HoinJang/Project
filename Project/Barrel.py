from pico2d import *

class Barrel:
    image = None
    def __init__(self):
        self.frame = 0
        if Barrel.image == None :
            Barrel.image = load_image('Resource/Barrel.png')
    def draw(self):
        self.image.clip_draw(self.frame * 30, 0, 30, 30, 30, 455)
    def update(self):
        self.frame +=1
        if(self.frame > 7):
            self.frame = 0
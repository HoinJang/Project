from pico2d import *

class Potal:
    image = None
    def __init__(self):
        self.frame = 0
        if Potal.image == None:
            Potal.image = load_image('Resource/Potal.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 50, 100, 465)
    def update(self):
        self.frame +=1
        if(self.frame > 7):
            self.frame = 0
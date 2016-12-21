import Macro

from pico2d import *

class Unbeat:
    image = None
    sound = None
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.collideon = False
        if Unbeat.image == None:
            Unbeat.image = load_image('Resource/ItemUnbeat.png')
        if Unbeat.sound == None:
            Unbeat.sound = load_wav('Sound/GetUnbeat.wav')
    def draw(self):
        if self.collideon == False:
            self.image.draw(self.x, self.y)
    def draw_bb(self):
        if self.collideon == False:
            draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - Macro.item_size/2, self.y - Macro.item_size/2 , self.x + Macro.item_size/2, self.y + Macro.item_size/2
    def collide(self, b):
        left_a, bottom_a, right_a, top_a = self.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b : return False
        if right_a < left_b : return False
        if top_a < bottom_b : return False
        if bottom_a > top_b : return False
        return True
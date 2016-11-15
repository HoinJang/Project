import Macro

from pico2d import *

class Ladder:
    image = None
    def __init__(self,x,y):
        self.x, self.y = x,y
        if Ladder.image == None:
            Ladder.image = load_image('Resource/Ladder.png')
    def draw(self):
        self.image.draw(self.x, self.y)
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - Macro.ladder_width / 2 + 15, self.y - Macro.ladder_height/ 2, self.x + Macro.ladder_width / 2 - 15, self.y + Macro.ladder_height / 2
    def collide(self, b):
        left_a, bottom_a, right_a, top_a = self.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b: return False
        if right_a < left_b: return False
        if top_a < bottom_b: return False
        if bottom_a > top_b: return False
        return True
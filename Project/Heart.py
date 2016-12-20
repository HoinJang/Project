import Macro

from pico2d import *

class Heart:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5
    image = None
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.total_frames = 0
        self.collideon = False
        if Heart.image == None:
            Heart.image = load_image('Resource/ItemHeart.png')
    def draw(self):
        if self.collideon == False:
            self.image.clip_draw(self.frame * 30, 0, 30, 30, self.x, self.y)
    def update(self,frame_time):
        self.total_frames += Heart.FRAMES_PER_ACTION * Heart.ACTION_PER_TIME * frame_time /1.5
        self.frame = int(self.total_frames) % 7
        if (self.frame > 9):
            self.frame = 0
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
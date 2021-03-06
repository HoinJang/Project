import Macro

from pico2d import *

class Potal:
    PIXEL_PER_METER = (10.0/0.3)
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
        if Potal.image == None:
            Potal.image = load_image('Resource/Potal.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 50, self.x, self.y)
    def update(self, frame_time):
        self.total_frames += Potal.FRAMES_PER_ACTION * Potal.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7
        if(self.frame > 7):
            self.frame = 0
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - Macro.potal_size+ 5, self.y - Macro.potal_size/ 2 + 5, self.x +Macro.potal_size -5 , self.y + Macro.potal_size / 2 - 5
    def collide(self, b):
        left_a, bottom_a, right_a, top_a = self.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()
        if left_a > right_b : return False
        if right_a < left_b : return False
        if top_a < bottom_b : return False
        if bottom_a > top_b : return False
        return True
import Macro
from pico2d import *

class Barrel():
    PIXEL_PER_METER = (10.0/0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 7
    image = None

    def __init__(self,stage):
        self.frame = 0
        self.x = 50
        self.y = 515
        self.dx = 5
        self.dy = 5
        self.total_frames = 0
        self.stage = stage
        if Barrel.image == None :
            Barrel.image = load_image('Resource/Barrel.png')
    def update(self, frame_time):
        self.total_frames += Barrel.FRAMES_PER_ACTION * Barrel.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7
        if self.y == 515:
            self.x += self.dx
        elif self.y == 365:
            self.x -= self.dx
        elif self.y == 215:
            self.x += self.dx
        elif self.y == 65:
            self.x -= self.dx
        if self.x >= 770:
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
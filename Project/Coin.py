import json
import Macro

from pico2d import *

class Coin:
    PIXEL_PER_METER = (10.0 / 0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5
    image = None
    sound = None
    def __init__(self,x,y):
        self.x, self.y = x,y
        self.frame = 0
        self.total_frames = 0
        self.collideon = False
        if Coin.image == None:
            Coin.image = load_image('Resource/Coin.png')
        if Coin.sound == None:
            Coin.sound = load_wav('Sound/GetCoin.wav')
    def draw(self):
        if(self.collideon == False):
            self.image.clip_draw(self.frame * Macro.coin_size, 0, Macro.coin_size, Macro.coin_size, self.x, self.y)
    def update(self,frame_time):
        self.total_frames += Coin.FRAMES_PER_ACTION * Coin.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7
        if (self.frame > 6):
            self.frame = 0
    def draw_bb(self):
        if(self.collideon == False):
            draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - Macro.coin_size/2, self.y - Macro.coin_size/2 , self.x + Macro.coin_size/2, self.y + Macro.coin_size/2
    def collide(self, b):
        left_a, bottom_a, right_a, top_a = self.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()

        if left_a > right_b : return False
        if right_a < left_b : return False
        if top_a < bottom_b : return False
        if bottom_a > top_b : return False
        return True
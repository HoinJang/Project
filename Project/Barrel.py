import Macro
import random
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
        self.stage = stage
        self.frame = 0
        self.num = random.randint(1,4)
        self.left = False
        if self.stage == 1 or self.stage == 2:
            self.x = 750
            self.y = 405
        elif self.stage == 3:
            self.x = 800
            self.y = 495
        elif self.stage == 4:
            if self.num == 1:
                self.x, self.y = 170,650
            elif self.num == 2:
                self.x, self.y = 330,650
            elif self.num == 3:
                self.x, self.y = 470,650
            elif self.num == 4:
                self.x, self.y = 630,650
        elif self.stage == 5:
            if self.num == 1:
                self.x, self.y = 60, 650
            elif self.num == 2:
                self.x, self.y = 170, 650
            elif self.num == 3:
                self.x, self.y = 270, 650
            elif self.num == 4:
                self.x, self.y = 470, 650
        self.dx = 5
        self.dy = 5
        self.total_frames = 0
        self.collideon = False
        if Barrel.image == None :
            Barrel.image = load_image('Resource/Barrel.png')
    def update(self, frame_time):
        self.total_frames += Barrel.FRAMES_PER_ACTION * Barrel.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 7
        if self.stage == 1 or self.stage == 2:
            if self.y == 405:
                self.x -= self.dx
            elif self.y == 315:
                self.x += self.dx
            elif self.y == 225:
                self.x -= self.dx
            elif self.y == 135:
                self.x += self.dx
            elif self.y == 50:
                self.x -= self.dx
            if self.x >= 770:
                self.y -= self.dy
            if self.x <= 30:
                if self.y != 50:
                    self.y -= self.dy
            if(self.frame > 7):
                self.frame = 0
        elif self.stage == 3:
            if self.y == 495:
                self.x -= self.dx
            if self.x == 180:
                self.y -= self.dy
            if self.y == 230:
                self.x += self.dx
            if self.y < 300 and self.x == 220:
                self.y -= self.dy
            if self.y == 50:
                self.x += self.dx
            if self.y < 100 and self.x == 270:
                self.y -= self.dy
        elif self.stage == 4 :
            if self.num == 1:
                if self.y == 225 and self.x>=170 and self.x<=215:
                    self.x += self.dx
                else:
                    self.y -=self.dy
            elif self.num == 2:
                self.y -= self.dy
            elif self.num == 3:
                if self.y == 225 and self.x>=470 and self.x<=520:
                    self.x += self.dx
                else:
                    self.y -=self.dy
            elif self.num == 4:
                self.y -= self.dy
        elif self.stage == 5 :
            if self.y == 140:
                if(self.left):
                    self.x += self.dx
                    if(self.x > 540):
                        self.left = False
                elif(self.left == False):
                    self.x -= self.dx
                    if(self.x < 60):
                        self.left = True
            else:
                if self.num == 1:
                    self.y -=self.dy
                elif self.num == 2:
                    self.y -= self.dy
                elif self.num == 3:
                    self.y -=self.dy
                elif self.num == 4:
                    self.y -= self.dy

    def draw(self):
        if self.collideon == False:
            self.image.clip_draw(self.frame * 30, 0, 30, 30, self.x, self.y)

    def draw_bb(self):
        if self.collideon == False:
            draw_rectangle(*self.get_bb())
    def get_bb(self):
        return self.x - Macro.barrel_size/ 2 + 5, self.y - Macro.barrel_size/ 2 + 5, self.x +Macro.barrel_size/ 2 -5 , self.y + Macro.barrel_size / 2 - 5
from pico2d import *
import Macro
import GameOver_State_HI
import Framework_JHI

class Character:
    PIXEL_PER_METER = (10.0/0.3) # 24M*18M
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    image = None
    Jsound = None
    Csound = None
    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND , LEFT_JUMP, RIGHT_JUMP, LADDER_UP, LADDER_DOWN, LADDER_STAND = 0, 1, 2, 3, 4, 5, 6, 7, 8

    def __init__(self,x,y):
        self.x, self.y = x, y
        self.dy = 0
        self.hp = 5
        self.jump_possible = False
        self.jump = False
        self.imagestate = 2
        self.frame = 4
        self.state = self.RIGHT_STAND
        self.life_time = 0
        self.total_frames = 0
        self.gravity = True
        self.collide_ladder_x = 0
        self.collide_ladder_y = 0
        self.LRmove = False
        self.UDmove = False
        self.unbeat = False
        self.unbeat_time = 0
        if Character.image == None:
            Character.image = load_image('Resource/Player1.png')
        if Character.Jsound == None:
            Character.Jsound = load_wav('Sound/Jump.wav')
        if Character.Csound == None:
            Character.Csound = load_wav('Sound/Hpminus.wav')

    def handle_left_stand(self,distance):
        self.state = self.LEFT_STAND
        self.imagestate = 3
        self.frame = 4
    def handle_right_stand(self,distance):
        self.state = self.RIGHT_STAND
        self.imagestate = 2
        self.frame = 4
    def handle_left_run(self,distance):
        self.state = self.LEFT_RUN
        self.imagestate = 3
        self.x = max(0, self.x - distance)
        self.frame += 1
        if self.frame > 3:
            self.frame = 0
    def handle_right_run(self,distance):
        self.state = self.RIGHT_RUN
        self.imagestate = 2
        self.x = min(800, self.x + distance)
        self.frame += 1
        if self.frame > 3:
            self.frame = 0
    def handle_ladder_stand(self,distance):
        self.state = self.LADDER_STAND
        self.imagestate = 1
        self.frame = 4
    def handle_ladder_up(self,distance):
            self.imagestate = 1
            self.y = min(self.collide_ladder_y + Macro.ladder_height/2 + Macro.player_size/2 - 10, self.y + distance)
            self.frame +=1
            if self.frame > 1:
                self.frame = 0
            if self.y == self.collide_ladder_y + Macro.ladder_height/2 + Macro.player_size/2 - 10:
                self.state = self.LEFT_STAND
    def handle_ladder_down(self,distance):
            self.imagestate = 1
            self.y = max(self.collide_ladder_y - Macro.ladder_height/2 + Macro.player_size/2 - 10, self.y - distance)
            self.frame +=1
            if self.frame > 1:
                self.frame = 0
            if self.y == self.collide_ladder_y - Macro.ladder_height/2 + Macro.player_size/2 - 10:
                self.state = self.RIGHT_STAND
    def handle_left_jump(self,distance):
        self.imagestate = 3
        self.frame = 0
        self.x = max(0, self.x - distance/1.5)
        if self.jump :
            self.dy += distance * 2
            if (self.dy > 50):
                self.jump = False
        self.dy -= distance
        if (self.dy < 0):
            self.state = self.LEFT_STAND
            self.dy = 0

    def handle_right_jump(self,distance):
        self.imagestate = 2
        self.frame = 3
        self.x = min(800, self.x + distance/1.5)
        if self.jump :
            self.dy += distance * 2
            if (self.dy > 50):
                self.jump = False
        self.dy -= distance
        if (self.dy < 0):
            self.state = self.RIGHT_STAND
            self.dy = 0

    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        LADDER_UP:handle_ladder_up,
        LADDER_DOWN:handle_ladder_down,
        LADDER_STAND:handle_ladder_stand,
        LEFT_JUMP: handle_left_jump,
        RIGHT_JUMP:handle_right_jump
    }
    def handle_event(self,event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN,):
                if self.LRmove :
                    self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN,):
                if self.LRmove:
                    self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                if self.LRmove :
                    self.state = self.RIGHT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                if self.LRmove :
                    self.state = self.LEFT_STAND
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if(self.x > self.collide_ladder_x - Macro.ladder_width/2 + 5 and self.x < self.collide_ladder_x + Macro.ladder_width/2 - 5
               and self.y >= self.collide_ladder_y - Macro.ladder_height/2 - Macro.player_size/2 and self.y <= self.collide_ladder_y + Macro.ladder_height/2 + Macro.player_size/2):
                if self.UDmove:
                    self.state = self.LADDER_UP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if(self.x > self.collide_ladder_x - Macro.ladder_width/2 + 5 and self.x < self.collide_ladder_x + Macro.ladder_width/2 - 5
               and self.y >= self.collide_ladder_y - Macro.ladder_height/2 - Macro.player_size/2 and self.y <= self.collide_ladder_y + Macro.ladder_height/2 + Macro.player_size/2):
                if self.UDmove:
                    self.state = self.LADDER_DOWN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.LADDER_UP, self.LADDER_DOWN):
                if self.UDmove:
                    self.state = self.LADDER_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.LADDER_UP, self.LADDER_DOWN):
                if self.UDmove:
                    self.state = self.LADDER_STAND
        elif (event.type, event.key) == (SDL_KEYDOWN,SDLK_SPACE):
            if self.state in (self.RIGHT_RUN,self.RIGHT_STAND):
                self.state = self.RIGHT_JUMP
                self.jump = True
                self.Jsound.set_volume(10)
                self.Jsound.play()
            elif self.state in (self.LEFT_RUN, self.LEFT_STAND):
                self.state = self.LEFT_JUMP
                self.jump = True
                self.Jsound.set_volume(10)
                self.Jsound.play()
        pass
    def update(self, frame_time):

        self.life_time += frame_time
        distance = Character.RUN_SPEED_PPS * frame_time
        self.total_frames += Character.FRAMES_PER_ACTION * Character.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5
        self.handle_state[self.state](self, distance)
        if(self.gravity):
            self.y -= distance
        if(self.unbeat):
            self.unbeat_time +=1
            if(self.unbeat_time > 500):
                self.unbeat_time = 0
                self.unbeat = False
        pass
    def draw(self):
        self.image.clip_draw(self.frame * Macro.player_size, self.imagestate * Macro.player_size, Macro.player_size, Macro.player_size, self.x, self.y + self.dy)
    def get_bb(self):
        return self.x - Macro.player_size/2 + 15, self.y - Macro.player_size/2 + 5 + self.dy, self.x +Macro.player_size/2 - 15 , self.y + self.dy
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
from pico2d import *
import Macro


class Player:

    PIXEL_PER_METER = (10.0/0.3)
    RUN_SPEED_KMPH = 20.0
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 5

    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_JUMP, RIGHT_JUMP, LADDER_UP, LADDER_DOWN, LADDER_STAND  = 0, 1, 2, 3, 4, 5, 6, 7, 8

    def __init__(self):
        self.x, self.y = 75, 150
        self.imagestate = 2
        self.frame = 4
        self.state = self.RIGHT_STAND
        self.jump = False
        self.total_frames = 0
        self.beforejump = 0
        self.gravity = True
        self.collide_ladder_x = 0
        self.collide_ladder_y = 0
        self.life_time = 0


        if Player.image == None:
            Player.image = load_image('Resource/Player1.png')
    def update(self, frame_time):
        self.life_time += frame_time
        distance = Player.RUN_SPEED_PPS * frame_time
        self.total_frames += Player.FRAMES_PER_ACTION * Player.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 5
        self.handle_state[self.state](self, distance)
        if self.gravity:
            self.y -= distance
    def handle_left_stand(self,distance):
        self.state = self.LEFT_STAND
        self.imagestate = 3
        self.beforejump = self.y
        self.frame = 4
        self.jump = False
    def handle_right_stand(self,distance):
        self.state = self.RIGHT_STAND
        self.imagestate = 2
        self.beforejump = self.y
        self.frame = 4
        self.jump = False
    def handle_ladder_stand(self,distance):
        self.state = self.LADDER_STAND
        self.imagestate = 1
        self.frame = 4
    def handle_left_run(self,distance):
        self.state = self.LEFT_RUN
        self.imagestate = 3
        self.beforejump = self.y
        self.x = max(0, self.x - distance)
        self.frame += 1
        if self.frame > 3:
            self.frame = 0
        self.jump = False
    def handle_right_run(self,distance):
        self.state = self.RIGHT_RUN
        self.imagestate = 2
        self.beforejump = self.y
        self.x = min(800, self.x + distance)
        self.frame += 1
        if self.frame > 3:
            self.frame = 0
        self.jump = False
    def handle_left_jump(self,distance):
        self.imagestate = 3
        self.frame = 0
        self.x = max(0, self.x - distance/2)
        if (self.jump == False):
            self.y += distance
            if (self.y > self.beforejump + 70):
                self.jump = True
        if (self.jump == True):
            self.gravity = True
            if (self.y < self.beforejump):
                self.gravity = False
                self.state = self.LEFT_STAND
                self.y = self.beforejump
    def handle_right_jump(self,distance):
        self.imagestate = 2
        self.frame = 3
        self.x = min(800, self.x + distance/2)
        if (self.jump == False):
            self.y += distance
            if (self.y > self.beforejump + 70):
                self.jump = True
        if (self.jump == True):
            self.gravity = True
            if (self.y < self.beforejump):
                self.gravity = False
                self.state = self.RIGHT_STAND
                self.y = self.beforejump
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
    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        LEFT_JUMP: handle_left_jump,
        RIGHT_JUMP:handle_right_jump,
        LADDER_UP:handle_ladder_up,
        LADDER_DOWN:handle_ladder_down,
        LADDER_STAND:handle_ladder_stand
    }
    def handle_event(self,event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.RIGHT_RUN,):
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND, self.LEFT_RUN,):
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.RIGHT_RUN,self.RIGHT_STAND):
                self.state = self.RIGHT_JUMP
            elif self.state in (self.LEFT_RUN, self.LEFT_STAND):
                self.state = self.LEFT_JUMP
        if (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            if(self.x > self.collide_ladder_x - Macro.ladder_width/2 + 15 and self.x < self.collide_ladder_x + Macro.ladder_width/2 - 15
               and self.y >= self.collide_ladder_y - Macro.ladder_height/2 - Macro.player_size/2 and self.y <= self.collide_ladder_y + Macro.ladder_height/2 + Macro.player_size/2):
                self.state = self.LADDER_UP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            if(self.x > self.collide_ladder_x - Macro.ladder_width/2 + 15 and self.x < self.collide_ladder_x + Macro.ladder_width/2 - 15
               and self.y >= self.collide_ladder_y - Macro.ladder_height/2 - Macro.player_size/2 and self.y <= self.collide_ladder_y + Macro.ladder_height/2 + Macro.player_size/2):
                self.state = self.LADDER_DOWN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            if self.state in (self.LADDER_UP, self.LADDER_DOWN):
                self.state = self.LADDER_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            if self.state in (self.LADDER_UP, self.LADDER_DOWN):
                self.state = self.LADDER_STAND
    def draw(self):
        self.image.clip_draw(self.frame * Macro.player_size, self.imagestate * Macro.player_size, Macro.player_size, Macro.player_size, self.x, self.y)
    def get_bb(self):
        return self.x - Macro.player_size/2 + 5, self.y - Macro.player_size/2 + 5, self.x +Macro.player_size/2 -5 , self.y +Macro.player_size/2
    def draw_bb(self):
        draw_rectangle(*self.get_bb())
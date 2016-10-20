from pico2d import *


class Player:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_JUMP, RIGHT_JUMP, LADDER_UP, LADDER_DOWN, LADDER_STAND  = 0, 1, 2, 3, 4, 5, 6, 7, 8

    def handle_left_run(self):
        self.state = self.LEFT_RUN
        self.imagestate = 3
        self.beforejump = self.y
        self.x = max(0, self.x - 3)
        self.frame += 1
        if self.frame > 3:
            self.frame = 0
    def handle_left_stand(self):
        self.state = self.LEFT_STAND
        self.imagestate = 3
        self.beforejump = self.y
        self.frame = 4
    def handle_right_run(self):
        self.state = self.RIGHT_RUN
        self.imagestate = 2
        self.beforejump = self.y
        self.x = min(800, self.x + 3)
        self.frame += 1
        if self.frame > 3:
            self.frame = 0
    def handle_right_stand(self):
        self.state = self.RIGHT_STAND
        self.imagestate = 2
        self.beforejump = self.y
        self.frame = 4
    def handle_left_jump(self):
        self.imagestate = 3
        self.frame = 0
        self.x = max(0, self.x - 1)
        if (self.jump == False):
            self.y += 5
            if (self.y >= self.beforejump + 70):
                self.jump = True
        if (self.jump == True):
            self.y -= 5
            if (self.y < self.beforejump):
                self.y = self.beforejump
                self.state = self.LEFT_STAND
                self.jump = False
    def handle_right_jump(self):
        self.imagestate = 2
        self.frame = 3
        self.x = min(800, self.x + 1)
        if (self.jump == False):
            self.y += 5
            if (self.y >= self.beforejump + 70):
                self.jump = True
        if (self.jump == True):
            self.y -= 5
            if (self.y < self.beforejump):
                self.y = self.beforejump
                self.state = self.RIGHT_STAND
                self.jump = False
    def handle_ladder_up(self):
        self.state = self.LADDER_UP
        self.imagestate = 1
        self.y +=1
        self.frame +=1
        if self.frame > 1:
            self.frame = 0
    def handle_ladder_down(self):
        self.state = self.LADDER_DOWN
        self.imagestate = 1
        self.y -=1
        self.frame +=1
        if self.frame > 1:
            self.frame = 0
    def handle_ladder_stand(self):
        self.state = self.LADDER_STAND
        self.imagestate = 1
        self.frame = 4
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
    def __init__(self):
        self.x, self.y = 750, 50
        self.imagestate = 2
        self.frame = 4
        self.state = self.RIGHT_STAND
        self.jump = False
        self.beforejump = 0
        if Player.image == None:
            Player.image = load_image('Resource/Player1.png')
    def handle_event(self,event):
        if(event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.LEFT_RUN
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            if self.state in (self.RIGHT_STAND, self.LEFT_STAND):
                self.state = self.RIGHT_RUN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            if self.state in (self.RIGHT_RUN,):
                self.state = self.RIGHT_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            if self.state in (self.LEFT_RUN,):
                self.state = self.LEFT_STAND
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_UP):
            self.state = self.LADDER_UP
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_DOWN):
            self.state = self.LADDER_DOWN
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_UP):
            self.state = self.LADDER_STAND
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_DOWN):
            self.state = self.LADDER_STAND
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.RIGHT_RUN,self.RIGHT_STAND):
                self.state = self.RIGHT_JUMP
            elif self.state in (self.LEFT_RUN, self.LEFT_STAND):
                self.state = self.LEFT_JUMP
    def update(self):
        self.handle_state[self.state](self)
    def draw(self):
        self.image.clip_draw(self.frame * 50, self.imagestate * 50, 50, 50, self.x, self.y+15)

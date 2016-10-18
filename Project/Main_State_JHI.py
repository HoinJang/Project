import random
import json
import os

from pico2d import *

import Framework_JHI
import Title_State_JHI

name = "MainState"

player = None
ground = None
block = None
potal = None
running = None
background = None

class BackGround:
    image = None
    def __init__(self):
        self.x1 = 400
        self.x2 = 1200
        if BackGround.image == None:
            BackGround.image = load_image('Resource/BackGround.png')
    def draw(self):
        self.image.draw(self.x1,300)
        self.image.draw(self.x2,300)
    def update(self):
        self.x1 -= 1
        self.x2 -= 1
        if self.x1 == -400:
            self.x1 = 1200
        if self.x2 == -400:
            self.x2 = 1200
class Potal:
    image = None
    def __init__(self):
        self.frame = 0
        if Potal.image == None:
            Potal.image = load_image('Resource/Potal.png')
    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 50, 100, 485)
    def update(self):
        self.frame +=1
        if(self.frame > 7):
            self.frame = 0
class Block:
    image = None
    def __init__(self):
        if Block.image == None:
            Block.image = load_image('Resource/Block.png')
    def draw(self):
        self.image.draw(350,175)
        self.image.draw(425,310)
        self.image.draw(350,445)
class Ground:
    image = None
    def __init__(self):
        if Ground.image == None:
            Ground.image = load_image('Resource/Ground.png')
    def draw(self):
        self.image.draw(400, 25)
class Player:
    image = None

    LEFT_RUN, RIGHT_RUN, LEFT_STAND, RIGHT_STAND, LEFT_JUMP, RIGHT_JUMP = 0, 1, 2, 3, 4,5

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
            self.y += 3
            if (self.y >= self.beforejump + 70):
                self.jump = True
        if (self.jump == True):
            self.y -= 3
            if (self.y < self.beforejump):
                self.y = self.beforejump
                self.state = self.LEFT_STAND
                self.jump = False
    def handle_right_jump(self):
        self.imagestate = 2
        self.frame = 3
        self.x = min(800, self.x + 1)
        if (self.jump == False):
            self.y += 3
            if (self.y >= self.beforejump + 70):
                self.jump = True
        if (self.jump == True):
            self.y -= 3
            if (self.y < self.beforejump):
                self.y = self.beforejump
                self.state = self.RIGHT_STAND
                self.jump = False
    handle_state = {
        LEFT_RUN: handle_left_run,
        RIGHT_RUN: handle_right_run,
        LEFT_STAND: handle_left_stand,
        RIGHT_STAND: handle_right_stand,
        LEFT_JUMP: handle_left_jump,
        RIGHT_JUMP:handle_right_jump,
    }
    def __init__(self):
        self.x, self.y = 300, 60
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
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            if self.state in (self.RIGHT_RUN,self.RIGHT_STAND):
                self.state = self.RIGHT_JUMP
            elif self.state in (self.LEFT_RUN, self.LEFT_STAND):
                self.state = self.LEFT_JUMP
    def update(self):
        self.handle_state[self.state](self)
    def draw(self):
        self.image.clip_draw(self.frame * 50, self.imagestate * 50, 50, 50, self.x, self.y)

def enter():
    global player
    global running
    global ground
    global block
    global potal
    global background
    background = BackGround()
    player = Player()
    ground = Ground()
    block = Block()
    potal = Potal()
    running = True
    pass


def exit():
    global player,ground,block,potal,background
    del(player)
    del(ground)
    del(block)
    del(potal)
    del(background)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    global player
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework_JHI.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                Framework_JHI.quit()
        else:
            player.handle_event(event)
    pass


def update():
    player.update()
    potal.update()
    background.update()
    delay(0.01)
    pass


def draw():
    clear_canvas()
    background.draw()
    potal.draw()
    ground.draw()
    block.draw()
    player.draw()
    update_canvas()
    pass



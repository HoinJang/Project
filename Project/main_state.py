import random
import json
import os

from pico2d import *

import game_framework
import title_state



name = "MainState"

boy = None
grass = None
font = None



class Grass:
    def __init__(self):
        self.image = load_image('Resource/grass.png')

    def draw(self):
        self.image.draw(400, 30)



class Boy:

    def __init__(self):
        self.x, self.y = 100, 90
        self.frame = 0
        self.status = 2
        self.image = load_image('Resource/Player1.png')
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.leftstand = False
        self.rightstand = True
    def update(self):
        if self.leftstand == True or self.rightstand == True:
            self.frame = 0
        pass

    def draw(self):
        if self.left == True or self.leftstand == True:
            self.image.clip_draw(self.frame * 100, self.status*100, 100, 100, self.x, self.y)
        elif self.right == True or self.rightstand == True:
            self.image.clip_draw(self.frame * 100, self.status*100, 100, 100, self.x, self.y)
        elif self.up==True or self.down==True:
            self.image.clip_draw(self.frame * 100, self.status*100, 100, 100, self.x, self.y)



def enter():
    global boy, grass
    boy = Boy()
    grass = Grass()
    pass


def exit():
    global boy,grass
    del(boy)
    del(grass)
    pass


def pause():
    pass


def resume():
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN
            if event.key == SDLK_ESCAPE:
                game_framework.change_state(title_state)

    pass


def update():
    boy.update()
    pass


def draw():
    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()
    pass






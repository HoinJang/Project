import random
import json
import os
import Block
from pico2d import *
import Framework_JHI
import MapInit

name = "Main"
map = None

def enter():
    global map
    map = MapInit.Map(1)
    pass
def exit():
    global map
    del(map)
    pass
def pause():
    pass

def resume():
    pass

def draw(frame_time):
    global map
    clear_canvas()
    map.draw()
    update_canvas()
    pass
def update(frame_time):
    global map
    map.update(frame_time)
    pass
def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework_JHI.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                Framework_JHI.quit()
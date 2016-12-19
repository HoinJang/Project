import random
import json
import os
import Block
import Macro
from pico2d import *
import Framework_JHI

name = "Main"
def enter():
    pass
def exit():
    pass
def pause():
    pass

def resume():
    pass

def draw(frame_time):
    clear_canvas()
    update_canvas()
    pass
def update(frame_time):
    pass
def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework_JHI.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                Framework_JHI.quit()
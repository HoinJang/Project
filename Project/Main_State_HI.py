import random
import json
import os
import Block
from pico2d import *
import Framework_JHI
import MapInit
import BackGround
import Player

name = "Main"
map = None
background = None


def enter():
    global map,background,player
    player = Player.Player()
    map = MapInit.Map(1)
    background = BackGround.BackGround()
    pass
def exit():
    global map,background,player

    del(player)
    del(background)
    del(map)
    pass
def pause():
    pass

def resume():
    pass

def draw(frame_time):
    global map,background,player
    clear_canvas()
    background.draw()
    map.draw()
    player.draw()
    update_canvas()
    pass
def update(frame_time):
    global map,player
    map.update(frame_time)
    player.update(frame_time)
    pass
def handle_events(frame_time):
    global map,player
    events = get_events()
    for event in events:
        player.handle_event(event)
        if event.type == SDL_QUIT:
            Framework_JHI.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                Framework_JHI.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_SPACE):
            map = MapInit.Map(2)
            player = Player.Player()


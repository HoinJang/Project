import random
import json
import os

from pico2d import *

import BackGround
import Potal
import Barrel
import Map
import Ground
import Player
import Macro
import Framework_JHI

# initialization code
name = "MainState"
player = None
ground = None
potal = None
running = None
background = None
barrel = None
map = None
time = 0

def enter():
    global player,running,ground,block,potal,background,barrels,map
    background = BackGround.BackGround()
    ground = Ground.Ground()
    map = Map.Map()
    potal = Potal.Potal()
    barrels = [Barrel() for i in range(0)]
    player = Player.Player()
    running = True

def exit():
    global player, ground, map, potal, background, barrels, hurdle
    del(player)
    del(ground)
    del(map)
    del(potal)
    del(background)
    del(barrels)

def pause():
    pass

def resume():
    pass

def draw():
    clear_canvas()
    background.draw()
    potal.draw()
    ground.draw()
    map.draw()
    for barrel in barrels:
        barrel.draw()
    player.draw()
    player.draw_bb()
    update_canvas()
def update():
    global time,barrels,map
    player.update()
    potal.update()
    background.update()
    time +=1
    if time%50 == 1:
        barrels += [Barrel.Barrel()]
    for barrel in barrels:
        barrel.update()
    for block in map.blocks:
        if block.collide(player):
            if(player.state != player.LEFT_JUMP and player.state != player.RIGHT_JUMP):
                player.setY(block.y + Macro.tile_size-5)
                print("collide")

    delay(0.01)

    return True
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
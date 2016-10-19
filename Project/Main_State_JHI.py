import random
import json
import os

from pico2d import *

import BackGround
import Potal
import Ladder
import Barrel
import Block
import Ground
import Player
import Macro

import Framework_JHI
import Title_State_JHI

# initialization code
name = "MainState"
ladder = None
player = None
ground = None
block = None
potal = None
running = None
background = None
barrel = None

def enter():
    global player
    global running
    global ground
    global block
    global potal
    global background
    global ladder
    global barrel
    ladder = Ladder.Ladder()
    background = BackGround.BackGround()
    ground = Ground.Ground()
    block = Block.Block()
    potal = Potal.Potal()
    barrel = Barrel.Barrel()
    player = Player.Player()
    running = True

def exit():
    global player, ground, block, potal, background, ladder, barrel
    del(player)
    del(ground)
    del(block)
    del(potal)
    del(background)
    del(ladder)
    del(barrel)

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

def update():
    player.update()
    potal.update()
    background.update()
    barrel.update()
    delay(0.01)

def draw():
    clear_canvas()
    background.draw()
    ladder.draw()
    potal.draw()
    ground.draw()
    block.draw()
    barrel.draw()
    player.draw()
    update_canvas()



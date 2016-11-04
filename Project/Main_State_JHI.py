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
time = 0

def enter():
    global player,running,ground,block,potal,background,ladder,barrels
    ladder = Ladder.Ladder()
    background = BackGround.BackGround()
    ground = Ground.Ground()
    block = Block.Block()
    potal = Potal.Potal()
    barrels = [Barrel() for i in range(0)]
    player = Player.Player()
    running = True

def exit():
    global player, ground, block, potal, background, barrels, hurdle
    del(player)
    del(ground)
    del(block)
    del(potal)
    del(background)
    del(ladder)
    del(barrels)

def pause():
    pass

def resume():
    pass

def draw():
    clear_canvas()
    background.draw()
    ladder.draw()
    potal.draw()
    ground.draw()
    block.draw()
    for barrel in barrels:
        barrel.draw()
    player.draw()
    update_canvas()
def update():
    global time,barrels
    player.update()
    potal.update()
    background.update()
    time +=1
    if time%50 == 1:
        barrels += [Barrel.Barrel()]

    for barrel in barrels:
        barrel.update()

    delay(0.01)

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





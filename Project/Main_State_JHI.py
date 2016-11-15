import random
import json
import os

from pico2d import *

import BackGround
import Potal
import Barrel
import Map
import Player
import Macro
import Framework_JHI

# initialization code
name = "MainState"
player = None
potal = None
running = None
background = None
barrel = None
map = None
time = 0

def enter():
    global player,running,block,potal,background,barrels,map
    background = BackGround.BackGround()
    map = Map.Map()
    potal = Potal.Potal()
    barrels = [Barrel() for i in range(0)]
    player = Player.Player()
    running = True

def exit():
    global player, map, potal, background, barrels, hurdle
    del(player)
    del(map)
    del(potal)
    del(background)
    del(barrels)

def pause():
    pass

def resume():
    pass

def draw(frame_time):
    clear_canvas()
    background.draw()
    potal.draw()
    map.draw()
    for barrel in barrels:
        barrel.draw()
        barrel.draw_bb()
    player.draw()
    player.draw_bb()
    update_canvas()

def update(frame_time):
    global time,barrels,map
    player.update(frame_time)
    potal.update()
    background.update()
    time += 1
    if time%100 == 1:
        barrels += [Barrel.Barrel()]
    for barrel in barrels:
        barrel.update()
    for block in map.blocks:
        if block.collide(player):
            player.gravity = False
    for ladder in map.ladders:
        if ladder.collide(player):
            player.collide_ladder_x = ladder.x
            player.collide_ladder_y = ladder.y
def handle_events(frame_time):
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
def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True
from pico2d import *
import Framework_JHI
import MapInit
import Character
import Barrel
import Macro

name = "Main"
map = None
stage = None
character = None
barrels = None
time = 0
dtime = None

def enter():
    global map,stage,character,barrels,dtime
    dtime = 100
    stage = 1
    map = MapInit.Map(stage)
    character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
    barrels = [Barrel() for i in range(0)]
    pass
def exit():
    global map,character,barrels
    del(map)
    del(character)
    del(barrels)
    pass
def pause():
    pass

def resume():
    pass

def draw(frame_time):
    global map,character,barrels
    clear_canvas()
    map.draw()
    for barrel in barrels:
        barrel.draw()
        barrel.draw_bb()
    character.draw()
    character.draw_bb()

    update_canvas()

def update(frame_time):
    global map,character,stage,time,barrels,dtime

    time += 1
    if time % dtime == 1:
        barrels += [Barrel.Barrel(stage)]
    for barrel in barrels:
        barrel.update(frame_time)
    ##################################
    character.update(frame_time)
    map.update(frame_time)
    print(character.x,character.y)
    for block in map.blocks:
        if block.collide(character):
            character.LRmove = True
            character.gravity = False
            break
        else:
            character.LRmove = False
    for ladder in map.ladders:
        if ladder.collide(character):
            character.collide_ladder_x = ladder.x
            character.collide_ladder_y = ladder.y
            if character.state != character.LEFT_JUMP and character.state != character.RIGHT_JUMP:
                character.UDmove = True
            break
        else:
            character.UDmove = False
    if character.LRmove == False and character.UDmove == False and character.state != character.LEFT_JUMP and character.state != character.RIGHT_JUMP:
        character.gravity = True
        if(character.state == character.RIGHT_RUN ):
            character.state = character.RIGHT_STAND
        elif(character.state == character.LEFT_RUN):
            character.state = character.LEFT_STAND
    for coin in map.coins:
        if coin.collide(character) and coin.collideon == False:
            coin.collideon = True
            print(1234)
    for heart in map.hearts:
        if heart.collide(character) and heart.collideon == False:
            heart.collideon = True
            print(1)
    for unbeat in map.unbeats:
        if unbeat.collide(character) and unbeat.collideon == False:
            unbeat.collideon = True
            print(2)
    for potal in map.potals:
        if potal.collide(character):
            if stage == 1:
                stage = 2
                map = MapInit.Map(stage)
                character = Character.Character(Macro.player_start_x2,Macro.player_start_y2)
                barrels = [Barrel() for i in range(0)]
            elif stage == 2:
                stage = 3
                map = MapInit.Map(stage)
                character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
            elif stage == 3:
                stage = 4
                map = MapInit.Map(stage)
                character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
                dtime = 10
            elif stage == 4:
                stage = 5
                map = MapInit.Map(stage)
                character = Character.Character(Macro.player_start_x2,Macro.player_start_y2)

def handle_events(frame_time):
    global map,stage,character,barrels,dtime
    events = get_events()
    for event in events:
        character.handle_event(event)
        if event.type == SDL_QUIT:
            Framework_JHI.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE):
                Framework_JHI.quit()
        elif (event.type == SDL_KEYDOWN and event.key == SDLK_F1):
            if stage == 1:
                stage = 2
                map = MapInit.Map(stage)
                character = Character.Character(Macro.player_start_x2,Macro.player_start_y2)
                barrels = [Barrel() for i in range(0)]
                dtime = 100
            elif stage == 2:
                stage = 3
                map = MapInit.Map(stage)
                character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
                barrels = [Barrel() for i in range(0)]
            elif stage == 3:
                stage = 4
                map = MapInit.Map(stage)
                character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
                barrels = [Barrel() for i in range(0)]
                dtime = 50
            elif stage == 4:
                stage = 5
                map = MapInit.Map(stage)
                character = Character.Character(Macro.player_start_x2,Macro.player_start_y2)
                barrels = [Barrel() for i in range(0)]
                dtime = 50


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

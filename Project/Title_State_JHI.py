import Framework_JHI
import Main_State_JHI
import Macro
import Main_State_HI

from pico2d import *


name = "TitleState"
image = None
stage = Macro.stage

def enter():
    global image, stage
    stage = 1
    image = load_image('Resource/Title.png')

def exit():
    global image
    del(image)

def handle_events(frame_time):
    global stage
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework_JHI.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN , SDLK_ESCAPE):
                Framework_JHI.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Macro.stage = 2
                Framework_JHI.change_state(Main_State_JHI)
    pass


def draw(frame_time):
    clear_canvas()
    image.draw(Macro.width / 2, Macro.height / 2)
    update_canvas()
    pass

def update(frame_time):
    pass


def pause():
    pass


def resume():
    pass







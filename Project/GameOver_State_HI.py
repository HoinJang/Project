import Framework_JHI
import Macro
import Main_State_HI
import Title_State_JHI

from pico2d import *


name = "OverState"
image = None

def enter():
    global image
    image = load_image('Resource/End.png')

def exit():
    global image
    del(image)

def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework_JHI.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN , SDLK_ESCAPE):
                Framework_JHI.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
                Framework_JHI.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Framework_JHI.change_state(Title_State_JHI)
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


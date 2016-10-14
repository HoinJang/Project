import Framework_JHI
import Main_State_JHI
from pico2d import *


name = "TitleState"
image = None
def enter():
    global image
    image = load_image('Resource/Title.png')
    pass


def exit():
    global image
    del(image)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework_JHI.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN , SDLK_ESCAPE):
                Framework_JHI.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Framework_JHI.change_state(Main_State_JHI)
    pass


def draw():
    clear_canvas()
    image.draw(400,300)
    update_canvas()
    pass

def update():
    pass


def pause():
    pass


def resume():
    pass







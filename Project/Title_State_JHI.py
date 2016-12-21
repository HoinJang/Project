import Framework_JHI
import Macro
import Main_State_HI
import Rank_State

from pico2d import *


name = "TitleState"
image = None
sound = None

def enter():
    global image, stage,sound
    stage = 1
    image = load_image('Resource/Title.png')
    sound = load_wav('Sound/Title.ogg')
    sound.set_volume(30)
    sound.play()

def exit():
    global image,sound
    del(image)
    del(sound)

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
                Framework_JHI.change_state(Main_State_HI)
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_r):
                Framework_JHI.change_state(Rank_State)
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







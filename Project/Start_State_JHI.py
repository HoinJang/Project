import Framework_JHI
import Title_State_JHI
import Macro
from pico2d import *


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(Macro.width, Macro.height, sync = True)
    if image == None:
        image = load_image('Resource/kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()

def update(frame_time):
    global logo_time
    if logo_time > 1.0 :
        logo_time = 0
        Framework_JHI.push_state(Title_State_JHI)
    delay(0.01)
    logo_time +=0.01

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(Macro.width / 2, Macro.height / 2)
    update_canvas()

def handle_events(frame_time):
    events = get_events()

def pause():
    pass


def resume():
    pass





import Framework_JHI
import Title_State_JHI
import json
from pico2d import *


name = "RankState"
image = None
font = None
def enter():
    global image
    global font
    image = load_image('Resource/blackboard.png')
    font = load_font('Resource/ENCR10B.TTF', 40)
def exit():
    global image
    global font
    del(image)
    del(font)
def pause():
    pass

def resume():
    pass
def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            Framework_JHI.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                Framework_JHI.change_state(Title_State_JHI)
def update(frame_time):
    pass

def draw_ranking():
    f = open('Data_File_Temp', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)
    score_data = score_data[:10]

    font.draw(280,500,'[RANKING]', (255,255,0))
    i = 0
    for score in score_data:
        font.draw(100,450-40*i,'TIME:%4.1f, X:%3d, Y:%3d'
                  % (score['Time'],score['X'],score['Y']), (100,150,150))
        i+=1
def bubble_sort(data):
    for i in range(0, len(data)):
         for j in range(0,len(data)):
            if(data[i]['Time']<data[j]['Time']):
                data[i], data[j] = data[j], data[i]

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    draw_ranking()
    update_canvas()


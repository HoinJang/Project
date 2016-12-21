import Framework_JHI
import Title_State_JHI
from pico2d import *


name = "RankState"
image = None
font = None
def enter():
    global image
    global font
    image = load_image('Resource/Rankboard.png')
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
        if (event.type, event.key) == (SDL_KEYDOWN , SDLK_ESCAPE):
            Framework_JHI.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_q):
            Framework_JHI.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            Framework_JHI.change_state(Title_State_JHI)
def update(frame_time):
    pass

def draw_ranking():
    f = open('Ranking_file', 'r')
    score_data = json.load(f)
    f.close()

    bubble_sort(score_data)
    score_data = score_data[:5]

    i = 0
    for score in score_data:
        font.draw(100,400-40*i,'%d. Score:%5d'
                  % (i+1,score['Score']), (250,250,250))
        i+=1

def bubble_sort(data):
    for i in range(0, len(data)):
         for j in range(0,len(data)):
            if(data[i]['Score']>data[j]['Score']):
                data[i], data[j] = data[j], data[i]

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    draw_ranking()
    update_canvas()


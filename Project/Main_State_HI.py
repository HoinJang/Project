from pico2d import *
import Framework_JHI
import MapInit
import Character
import Barrel
import Macro
import StageImage
import HPbar
import UnbeatTrue
import Rank_State
import GameOver_State_HI
name = "Main"
map = None
stage = None
character = None
barrels = None
time = None
dtime = None
stageimage = None
hpbar = None
unbeatbar = None
font = None
score = None
HP = None
StartSound = None
BGM = None
def enter():
    global map,stage,character,barrels,dtime,time,stageimage,hpbar,unbeatbar,font,score,HP,StartSound,BGM
    dtime = 100
    time = 0
    stage = 1
    score = 0
    HP = 5
    stageimage = StageImage.StageImage(1)
    map = MapInit.Map(stage)
    character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
    barrels = [Barrel() for i in range(0)]
    unbeatbar = UnbeatTrue.UnbeatTrue(True,character.x,character.y)
    hpbar = HPbar.HPbar(character.hp)
    font = load_font('Resource/ENCR10B.TTF', 20)
    Framework_JHI.reset_time()
    if StartSound == None :
        StartSound = load_wav('Sound/start.wav')
    StartSound.set_volume(30)
    StartSound.play()
    if BGM == None:
        BGM = load_wav('Sound/BGM.ogg')
    BGM.set_volume(20)
    BGM.repeat_play()

def exit():
    global map,character,barrels,stageimage,hpbar,unbeatbar,StartSound,BGM
    del(map)
    del(character)
    del(barrels)
    del(stageimage)
    del(hpbar)
    del(unbeatbar)
    del(StartSound)
    del(BGM)
    pass
def pause():
    pass

def resume():
    pass

def draw(frame_time):
    global map,character,barrels,stageimage,hpbar,unbeatbar,font,score
    clear_canvas()
    map.draw()
    for barrel in barrels:
        barrel.draw()
    character.draw()
    hpbar.draw()
    unbeatbar.draw()
    font.draw(Macro.width/2-50, Macro.height-10, 'Score:%d' % (score), (0, 0, 0))
    stageimage.draw()
    update_canvas()

def update(frame_time):
    global map,character,stage,time,barrels,dtime,stageimage,hpbar,unbeatbar,score,HP
    ####################################
    if character.y < 0 :
        HP -= 1
    hpbar = HPbar.HPbar(HP)
    unbeatbar = UnbeatTrue.UnbeatTrue(character.unbeat,character.x,character.y+character.dy)
    stageimage.update()
    time += 1
    if time % dtime == 1:
        barrels += [Barrel.Barrel(stage)]
    for barrel in barrels:
        barrel.update(frame_time)
    ##################################
    character.update(frame_time)
    map.update(frame_time)
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
            score += 100
            coin.sound.set_volume(40)
            coin.sound.play()
    for heart in map.hearts:
        if heart.collide(character) and heart.collideon == False:
            heart.collideon = True
            if HP < 5:
                HP += 1
            score += 1000
            heart.sound.set_volume(40)
            heart.sound.play()
    for unbeat in map.unbeats:
        if unbeat.collide(character) and unbeat.collideon == False:
            unbeat.collideon = True
            character.unbeat = True
            score += 1000
            unbeat.sound.set_volume(40)
            unbeat.sound.play()
    for barrel in barrels:
        if barrel.collide(character) and barrel.collideon == False:
            barrel.collideon = True
            if character.unbeat == False:
                HP -= 1
                character.Csound.set_volume(40)
                character.Csound.play()
            else:
                score += 100
                barrel.sound.set_volume(40)
                barrel.sound.play()

    for potal in map.potals:
        if potal.collide(character):
            if stage == 1:
                stage = 2
                map = MapInit.Map(stage)
                stageimage = StageImage.StageImage(2)
                character = Character.Character(Macro.player_start_x2,Macro.player_start_y2)
                barrels = [Barrel() for i in range(0)]
                dtime = 100
                time = 0
                StartSound.set_volume(30)
                StartSound.play()
            elif stage == 2:
                stage = 3
                map = MapInit.Map(stage)
                stageimage = StageImage.StageImage(3)
                character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
                barrels = [Barrel() for i in range(0)]
                dtime = 100
                time = 0
                StartSound.set_volume(30)
                StartSound.play()
            elif stage == 3:
                stage = 4
                map = MapInit.Map(stage)
                stageimage = StageImage.StageImage(4)
                character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
                barrels = [Barrel() for i in range(0)]
                dtime = 50
                time = 0
                StartSound.set_volume(30)
                StartSound.play()
            elif stage == 4:
                stage = 5
                map = MapInit.Map(stage)
                stageimage = StageImage.StageImage(5)
                character = Character.Character(Macro.player_start_x2,Macro.player_start_y2)
                barrels = [Barrel() for i in range(0)]
                dtime = 50
                time = 0
                StartSound.set_volume(30)
                StartSound.play()
            elif stage == 5:
                f = open('Ranking_file', 'r')
                score_data = json.load(f)
                f.close()
                score_data.append({"Score": score})
                f = open('Ranking_file', 'w')
                json.dump(score_data, f)
                f.close()
                Framework_JHI.change_state(Rank_State)

    if HP < 0:
        Framework_JHI.change_state(GameOver_State_HI)


def handle_events(frame_time):
    global map,stage,character,barrels,dtime,time,stageimage
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
                stageimage = StageImage.StageImage(2)
                character = Character.Character(Macro.player_start_x2,Macro.player_start_y2)
                barrels = [Barrel() for i in range(0)]
                dtime = 100
                time = 0
                StartSound.set_volume(30)
                StartSound.play()
            elif stage == 2:
                stage = 3
                map = MapInit.Map(stage)
                stageimage = StageImage.StageImage(3)
                character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
                barrels = [Barrel() for i in range(0)]
                dtime = 100
                time = 0
                StartSound.set_volume(30)
                StartSound.play()
            elif stage == 3:
                stage = 4
                map = MapInit.Map(stage)
                stageimage = StageImage.StageImage(4)
                character = Character.Character(Macro.player_start_x1,Macro.player_start_y1)
                barrels = [Barrel() for i in range(0)]
                dtime = 50
                time = 0
                StartSound.set_volume(30)
                StartSound.play()
            elif stage == 4:
                stage = 5
                map = MapInit.Map(stage)
                stageimage = StageImage.StageImage(5)
                character = Character.Character(Macro.player_start_x2,Macro.player_start_y2)
                barrels = [Barrel() for i in range(0)]
                dtime = 50
                time = 0
                StartSound.set_volume(30)
                StartSound.play()
            elif stage == 5:
                f = open('Ranking_file', 'r')
                score_data = json.load(f)
                f.close()
                score_data.append({"Score": score})
                f = open('Ranking_file', 'w')
                json.dump(score_data, f)
                f.close()
                Framework_JHI.change_state(Rank_State)



def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False
    return True

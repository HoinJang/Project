import json
from pico2d import *



class BlockImage:
    image = None
    def __init__(self):
        if BlockImage.image == None:
            BlockImage.image = load_image('Resource/BlockImage.png')


class Maptool:
    Stage = 1
    MapPosition = None
    def __init__(self):
        if self.Stage == 1:
            f = open('State1','r')
            self.MapPosition = json.load(f)
            f.close()




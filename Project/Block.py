import json
import Macro

from pico2d import *

class Block:
    image = None
    map_data1 = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0],[0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0]]

    def __init__(self):
        if Block.image == None:
            Block.image = load_image('Resource/BlockImage.png')
    def draw(self):
        for i in range(0,4):
            for j in range(0,16):
                if(self.map_data1[i][j] == 1):
                    self.image.draw(Macro.tile_size/2 + (j*Macro.tile_size), (150*i)+Macro.tile_size/2)

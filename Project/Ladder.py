import Macro

from pico2d import *

class Ladder:
    image = None
    ladder_data = [[1,1,1],[1,1,1],[1,1,1]]

    def __init__(self):
        if Ladder.image == None :
            Ladder.image = load_image('Resource/Ladder.png')
    def draw(self):
        for i in range(0, 3):
            for j in range(0, 3):
                if (self.ladder_data[i][j] == 1):
                    if(i !=1):
                        self.image.draw(Macro.ladder_width / 2 + ((j+1) * (Macro.ladder_width*2)), (150 * i) + Macro.ladder_height / 2 + Macro.ladder_height/3)
                    else:
                        self.image.draw(- Macro.ladder_width/2  + ((j + 1) * (Macro.ladder_width*2)),(150 * i) + Macro.ladder_height / 2 + Macro.ladder_height / 3)

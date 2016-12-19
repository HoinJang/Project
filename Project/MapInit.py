import Macro
import Block
import Ladder
import Potal

class Map:
    def __init__(self, stage):

        if stage == 1:
            #File Init To Tile
            f = open('Stage/Stage1', 'r')
            self.Map_data = f.readlines()
            f.close()
            #Tile, Ladder, Potal
            self.blocks = [Block() for i in range(0)]
            self.ladders = [Ladder() for i in range(0)]
            self.potal = Potal.Potal(150,565)
            for i in range(Macro.tile_hnumber):
                for j in range(Macro.tile_wnumber):
                    if self.Map_data[i][j] == '1':
                        self.blocks += [Block.Block(Macro.tile_wsize/2 + Macro.tile_wsize * j,Macro.tile_hsize/2 + Macro.tile_hsize*i)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*1)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*4)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*7)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*10)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*13)]

    def draw(self):
        for block in self.blocks:
            block.draw()
            block.draw_bb()
        for ladder in self.ladders:
            ladder.draw()
            ladder.draw_bb()
        self.potal.draw()

    def update(self, frame_time):
        self.potal.update(frame_time)
        pass
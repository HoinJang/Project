import Macro
import Block
import Ladder

class Map:
    def __init__(self):
        self.blocks = [Block() for i in range(0)]
        self.ladders = [Ladder() for i in range(0)]

        for i in range(Macro.tile_wnumber):
            for j in range(Macro.tile_hnumber):
                self.blocks += [Block.Block(Macro.tile_size/2 + Macro.tile_size * i,Macro.tile_size/2 + Macro.tile_size*j + j * 100)]

        for p in range(Macro.ladder_wnumber):
            for q in range(Macro.ladder_hnumber):
                if q == 1:
                    self.ladders += [Ladder.Ladder(Macro.ladder_width + (Macro.ladder_width * 2 * p), Macro.ladder_height/2 + Macro.ladder_height/3 + (Macro.ladder_height * q))]
                else :
                    self.ladders += [Ladder.Ladder(Macro.ladder_width * 2 + (Macro.ladder_width * 2 * p), Macro.ladder_height/2 + Macro.ladder_height/3 + (Macro.ladder_height * q))]

        self.blocks[2] = Block.Block(Macro.tile_delete,Macro.tile_delete)
        self.blocks[63] = Block.Block(Macro.tile_delete, Macro.tile_delete)
        self.blocks[61] = Block.Block(Macro.tile_delete,Macro.tile_delete)
        self.ladders[1] = Ladder.Ladder(Macro.ladder_delete,Macro.ladder_delete)
    def draw(self):
        for block in self.blocks:
            block.draw()
            block.draw_bb()
        for ladder in self.ladders:
            ladder.draw()
            ladder.draw_bb()
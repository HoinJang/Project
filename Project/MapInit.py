import Macro
import Block
import Ladder
import Potal
import Coin
import Heart
import Unbeat


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
            self.coins = [Coin() for i in range(0)]
            self.hearts = [Heart() for i in range(0)]
            self.unbeats = [Unbeat() for i in range(0)]
            self.potal = Potal.Potal(150,565)
            for i in range(Macro.tile_hnumber):
                for j in range(Macro.tile_wnumber):
                    if self.Map_data[i][j] == '1':
                        self.blocks += [Block.Block(Macro.tile_wsize/2 + Macro.tile_wsize * j,Macro.tile_hsize/2 + Macro.tile_hsize*i)]
                        self.coins += [Coin.Coin(Macro.tile_wsize/2 + Macro.tile_wsize * j,Macro.tile_hsize/2 + Macro.tile_hsize*i + 60)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*1)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*4)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*7)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*10)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*13)]
            self.hearts += [Heart.ItemHeart(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*1)]
            self.hearts += [Heart.ItemHeart(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*4)]
            self.hearts += [Heart.ItemHeart(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*7)]
            self.hearts += [Heart.ItemHeart(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*10)]
            self.hearts += [Heart.ItemHeart(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*13)]
            self.unbeats += [UnBeat.ItemUnbeat()]
            #Coin Delete Hard Coding
            self.coins[96] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[95] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[94] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[93] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[92] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[91] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[77] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[1] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[0] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[13] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[14] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[15] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[19] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[20] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[43] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[44] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[45] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[49] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[50] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[73] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[74] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[75] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[76] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[46] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[16] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)

    def draw(self):
        for coin in self.coins:
            coin.draw()
            coin.draw_bb()
        for block in self.blocks:
            block.draw()
            block.draw_bb()
        for ladder in self.ladders:
            ladder.draw()
            ladder.draw_bb()
        for heart in self.hearts:
            heart.draw()
            heart.draw_bb()
        for unbeat in self.unbeats:
            unbeat.draw()
            unbeat.draw_bb()
        self.potal.draw()

    def update(self, frame_time):
        self.potal.update(frame_time)
        for coin in self.coins:
            coin.update(frame_time)
        for heart in self.hearts:
            heart.update(frame_time)
        pass
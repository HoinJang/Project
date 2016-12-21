import Macro
import Block
import Ladder
import Potal
import Coin
import Heart
import Unbeat
import BackGround


class Map:
    def __init__(self, stage):
        self.stage = stage
        if self.stage == 1:
            #BackGround
            self.BackGround = BackGround.BackGround(1)
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
            self.potals = [Potal() for i in range(0)]
            for i in range(Macro.tile_hnumber):
                for j in range(Macro.tile_wnumber):
                    if self.Map_data[i][j] == '1':
                        self.blocks += [Block.Block(Macro.tile_wsize/2 + Macro.tile_wsize * j,Macro.tile_hsize/2 + Macro.tile_hsize*i)]
                        self.coins += [Coin.Coin(Macro.tile_wsize/2 + Macro.tile_wsize * j,Macro.tile_hsize/2 + Macro.tile_hsize*i + 65)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*1)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*4)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*7)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*10)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*13)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*1)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*4)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*7)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 3, Macro.ladder_height/2 + (Macro.tile_hsize)*10)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*13)]
            self.unbeats += [Unbeat.Unbeat(self.coins[90].x,self.coins[90].y)]
            self.unbeats += [Unbeat.Unbeat(self.coins[34].x,self.coins[34].y)]
            #Coin Delete Hard Coding
            self.coins[90] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[77] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[78] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
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
            self.coins[34] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.potals += [Potal.Potal(self.blocks[78].x,self.blocks[78].y+Macro.potal_size/2 + Macro.tile_hsize/2)]
        elif self.stage == 2:
            #BackGround
            self.BackGround = BackGround.BackGround(2)
            #File Init To Tile
            f = open('Stage/Stage2', 'r')
            self.Map_data = f.readlines()
            f.close()
            #Tile, Ladder, Potal
            self.blocks = [Block() for i in range(0)]
            self.ladders = [Ladder() for i in range(0)]
            self.coins = [Coin() for i in range(0)]
            self.hearts = [Heart() for i in range(0)]
            self.unbeats = [Unbeat() for i in range(0)]
            self.potals = [Potal() for i in range(0)]
            for i in range(Macro.tile_hnumber):
                for j in range(Macro.tile_wnumber):
                    if self.Map_data[i][j] == '1':
                        self.blocks += [Block.Block(Macro.tile_wsize/2 + Macro.tile_wsize * j,Macro.tile_hsize/2 + Macro.tile_hsize*i)]
                        self.coins += [Coin.Coin(Macro.tile_wsize/2 + Macro.tile_wsize * (j + 1),Macro.tile_hsize/2 + Macro.tile_hsize*i + 60)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 12, Macro.ladder_height/2 + (Macro.tile_hsize)*1)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 0, Macro.ladder_height/2 + (Macro.tile_hsize)*4)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*7)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 12, Macro.ladder_height/2 + (Macro.tile_hsize)*10)]
            self.ladders += [Ladder.Ladder(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*13)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 12 , Macro.ladder_height/2 + (Macro.tile_hsize)*1)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 0, Macro.ladder_height/2 + (Macro.tile_hsize)*4)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*7)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 12, Macro.ladder_height/2 + (Macro.tile_hsize)*10)]
            self.hearts += [Heart.Heart(Macro.ladder_width/2 + Macro.ladder_width * 11, Macro.ladder_height/2 + (Macro.tile_hsize)*13)]
            #self.unbeats += [Unbeat.Unbeat(self.coins[60].x,self.coins[60].y)]
            #self.unbeats += [Unbeat.Unbeat(self.coins[34].x,self.coins[34].y)]
            #Coin Delete Hard Coding
            self.potals += [Potal.Potal(self.blocks[35].x,self.blocks[35].y+Macro.potal_size/2 + Macro.tile_hsize/2)]
            self.coins[37] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[38] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[39] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[36] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[35] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[34] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[31] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[32] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[33] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[40] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[41] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[42] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[11] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[12] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[13] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
            self.coins[14] = Coin.Coin(Macro.NotDraw, Macro.NotDraw)
    def draw(self):
        self.BackGround.draw()
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
        for potal in self.potals:
            potal.draw()
            potal.draw_bb()
    def update(self, frame_time):
        for potal in self.potals:
            potal.update(frame_time)
        for coin in self.coins:
            coin.update(frame_time)
        for heart in self.hearts:
            heart.update(frame_time)
        pass
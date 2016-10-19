from pico2d import *

class Block:
    image = None
    def __init__(self):
        if Block.image == None:
            Block.image = load_image('Resource/Block.png')
    def draw(self):             #50 ~ 150
        self.image.draw(350,165) #180~280
        self.image.draw(425,295) #310~410
        self.image.draw(350,425)
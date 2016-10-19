from pico2d import *

class Ladder:
    image = None
    def __init__(self):
        if Ladder.image == None :
            Ladder.image = load_image('Resource/Ladder.png')
    def draw(self):
        self.image.draw(300, 100)
        self.image.draw(100, 100)
        self.image.draw(600, 100)
        self.image.draw(700, 230)
        self.image.draw(250, 230)
        self.image.draw(500, 230)
        self.image.draw(100, 360)
        self.image.draw(300, 360)
        self.image.draw(500, 360)
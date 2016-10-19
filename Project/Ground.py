from pico2d import *

class Ground:
    image = None
    def __init__(self):
        if Ground.image == None:
            Ground.image = load_image('Resource/Ground.png')
    def draw(self):
        self.image.draw(400, 25)
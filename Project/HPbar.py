from pico2d import *

class HPbar:
    image = None
    def __init__(self,hp):
            self.x = 600
            self.y = 575
            self.num = hp
            if HPbar.image == None:
                HPbar.image = load_image("Resource/HP.png")
    def draw(self):
        if self.num >= 5:
            self.image.draw(self.x, self.y)
        if self.num >= 4:
            self.image.draw(self.x + 45, self.y)
        if self.num >= 3:
            self.image.draw(self.x + 45 * 2, self.y)
        if self.num >= 2:
            self.image.draw(self.x + 45 * 3, self.y)
        if self.num >= 1:
            self.image.draw(self.x + 45 * 4, self.y)
    def update(self):
        pass

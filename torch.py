import pygame as pg


BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32
RADIUS = 4


class Torch(pg.sprite.Sprite):
    def __init__(self, x, y, id_block):
        pg.sprite.Sprite.__init__(self)
        self.id_block = id_block
        self.image = pg.Surface((32, 32))
        self.name = "torch"
        self.image = pg.image.load("data/texture/texture_wall/torch_wall_up_1.png").convert()
        self.rect = pg.Rect(x, y, 32, 32)
        self.x = x // BLOCK_WIDTH
        self.y = y // BLOCK_HEIGHT
        self.light_status = True

    def updated(self, layer_0, layer_1, layer_2):
        for e in layer_0:
            if e.x > self.x-RADIUS and e.x < self.x+RADIUS and e.y > self.y-RADIUS and e.y < self.y+RADIUS :
                e.light_status = True
        for e in layer_1:
            if e.x > self.x-RADIUS and e.x < self.x+RADIUS and e.y > self.y-RADIUS and e.y < self.y+RADIUS :
                e.light_status = True
        for e in layer_2:
            if e.x > self.x-RADIUS and e.x < self.x+RADIUS and e.y > self.y-RADIUS and e.y < self.y+RADIUS :
                e.light_status = True


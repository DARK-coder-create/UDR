import pygame as pg


BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32


class Wall(pg.sprite.Sprite):
    def __init__(self, x, y, id_block):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32, 64))
        self.id_block = id_block
        if id_block == 0:
            self.name = "wall_none"
            self.image = pg.image.load("data/texture/texture_wall/wall_none.png").convert()
            self.rect = pg.Rect(x, y, 32, 40)
        if id_block == 1:
            self.name = "wall_down_1"
            self.image = pg.image.load("data/texture/texture_wall/wall_down_1.png").convert()
            self.rect = pg.Rect(x, y, 32, 32)
        if id_block == 2:
            self.name = "wall_down_2"
            self.image = pg.image.load("data/texture/texture_wall/wall_down_2.png").convert()
            self.rect = pg.Rect(x, y, 32, 32)
        if id_block == 3:
            self.name = "wall_up_1"
            self.image = pg.image.load("data/texture/texture_wall/wall_up_1.png").convert()
            self.rect = pg.Rect(x, y, 32, 32)
        if id_block == 4:
            self.name = "wall_up_2"
            self.image = pg.image.load("data/texture/texture_wall/wall_up_2.png").convert()
            self.rect = pg.Rect(x, y, 32, 32)
            
        self.x = x // BLOCK_WIDTH
        self.y = y // BLOCK_HEIGHT
        self.light_status = False
        self.heath = 99999

    def info(self):
        pass

import pygame as pg


BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32


class Floor(pg.sprite.Sprite):
    def __init__(self, x, y, id_block):
        pg.sprite.Sprite.__init__(self)
        self.id_block = id_block
        if self.id_block <= 4:
            self.image = pg.Surface((32, 32))
            self.name = "floor_1"
            self.image = pg.image.load("data/texture/texture_floor/floor_1.png").convert()
            self.rect = pg.Rect(x, y, 32, 32)
        elif self.id_block == 5:
            self.image = pg.Surface((32, 32))
            self.name = "floor_2"
            self.image = pg.image.load("data/texture/texture_floor/floor_2.png").convert()
            self.rect = pg.Rect(x, y, 32, 32)
        elif self.id_block == 6:
            self.image = pg.Surface((32, 32))
            self.name = "floor_chest"
            self.image = pg.image.load("data/texture/texture_floor/floor_chest.png").convert()
            self.rect = pg.Rect(x, y, 32, 32)
        self.x = x // BLOCK_WIDTH
        self.y = y // BLOCK_HEIGHT
        self.light_status = False

    def info(self):
        pass

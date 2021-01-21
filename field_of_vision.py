import pygame as pg


BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32


class Field_of_vision(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((800, 600))
        self.image = pg.image.load("data/texture/texture_interface/field_of_vision_1.png").convert()
        self.rect = pg.Rect(x, y, 800, 600)

    def update(self, camera):
        self.rect.x = -camera.state.x
        self.rect.y = -camera.state.y

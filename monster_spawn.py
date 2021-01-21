import pygame as pg


class Monster_spawn(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.name = "monster_spawn"
        self.image = pg.image.load("data/texture/texture_floor/floor_spawn_monster.png").convert()
        self.rect = pg.Rect(x, y, 32, 32)
        self.x = x // 32
        self.y = y // 32
        self.light_status = False

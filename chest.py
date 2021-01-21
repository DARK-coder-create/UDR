import pygame as pg
import sqlite3
import random

class Chest(pg.sprite.Sprite):
    def __init__(self, x, y, id_block):
        pg.sprite.Sprite.__init__(self)
        self.id_block = id_block
        if self.id_block == 1:
            self.image = pg.Surface((32, 32))
            self.name = "bronze_chest"
            self.image = pg.image.load("data/texture/texture_chest/bronze_chest_close.png").convert()
        if self.id_block == 2:
            self.image = pg.Surface((32, 32))
            self.name = "holy_chest"
            self.image = pg.image.load("data/texture/texture_chest/holy_chest_close.png").convert()
        self.rect = pg.Rect(x, y, 32, 32)
        self.status = 'close'
        self.light_status = False
        self.x = x // 32
        self.y = y // 32
        self.heath = 99999

    def open(self):
        if self.status == 'close':
            con = sqlite3.connect("data/base_items.db")
            cursor = con.cursor()
            self.status = 'open'
            if self.id_block == 1:
                self.image = pg.image.load("data/texture/texture_chest/bronze_chest_open.png").convert()
                r = str(random.randint(1, 9))
                cursor.execute("SELECT * FROM weapon WHERE chance=?", r)
            if self.id_block == 2:
                self.image = pg.image.load("data/texture/texture_chest/holy_chest_open.png").convert()
                r = str(random.randint(1, 2))
                cursor.execute("SELECT * FROM potion WHERE chance=?", r)
            return cursor.fetchall()
            
            

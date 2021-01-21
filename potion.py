import pygame as pg

class Potion(pg.sprite.Sprite):
    def __init__(self, x, y, properties):
        pg.sprite.Sprite.__init__(self)
        self.name = "potion"
        self.name_potion = properties[0][0]
        self.properties = properties
        print(self.name)
        self.frequency = properties[0][2]
        self.speed = properties[0][3]
        self.type = properties[0][6]
        self.type_potion = properties[0][1]
        print(self.type)
        self.image = pg.Surface((32, 32))
        self.image = pg.image.load(str(properties[0][4])).convert()
        self.rect = pg.Rect(x, y, 32, 32)
        self.light_status = False

import pygame as pg

class Weapon(pg.sprite.Sprite):
    def __init__(self, x, y, properties):
        pg.sprite.Sprite.__init__(self)
        self.name = "weapon"
        self.name_weapon = properties[0][0]
        self.properties = properties
        print(self.name)
        self.damage = properties[0][1]
        self.frequency = properties[0][2]
        self.speed = properties[0][3]
        self.type = properties[0][6]
        print(self.type)
        self.image = pg.Surface((32, 32))
        self.image = pg.image.load(str(properties[0][4])).convert()
        self.rect = pg.Rect(x, y, 32, 32)
        self.light_status = False

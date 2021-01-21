import pygame as pg


BLOCK_WIDTH = 800
BLOCK_HEIGHT = 600


class Base_interface(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((800, 600))
        self.name = "base_interface"
        self.image = pg.image.load("data/texture/texture_interface/base_interface.png")
        self.rect = pg.Rect(x, y, 800, 600)
        self.heath = 96
        self.magia = 96
        self.image_bronze_4 = pg.image.load("data/texture/texture_weapon/none.png")
        self.image_4 = False
        self.properies_4 = None
        
        self.image_bronze_5 = pg.image.load("data/texture/texture_weapon/none.png")
        self.image_5 = False
        self.properies_5 = None

        self.image_holy_6 = pg.image.load("data/texture/texture_weapon/none.png")
        self.type_6 = None

        self.image_holy_7 = pg.image.load("data/texture/texture_weapon/none.png")
        self.type_7 = None

    def update(self, camera, screen):
        self.rect.x = -camera.state.x
        self.rect.y = -camera.state.y
        if self.heath > 96:
            self.heath = 96
        if self.heath < 0:
            self.heath = 0
        pg.draw.rect(screen, (255, 50, 50), pg.Rect(0, 96-self.heath, 96, self.heath))
        pg.draw.rect(screen, (50, 50, 255), pg.Rect(96, 96-self.magia, 96, self.magia))
        screen.blit(self.image_bronze_4, (626, 520))
        screen.blit(self.image_bronze_5, (663, 520))
        screen.blit(self.image_holy_6, (710, 520))
        screen.blit(self.image_holy_7, (748, 520))
        


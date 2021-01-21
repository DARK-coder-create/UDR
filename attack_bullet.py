import pygame as pg
import time

class Attack_bullet(pg.sprite.Sprite):
    def __init__(self, x, y, id_, direction, speed, attack, duration=1.5, where='hero'):
        pg.sprite.Sprite.__init__(self)
        self.id_block = id_
        self.where = where
        if self.id_block == 1:
            self.width = 16
            self.height = 64
            self.name = "attack_sword_1"
            self.image = pg.Surface((self.width, self.height))
            self.image = pg.image.load("data/texture/texture_attack/attack_sword_1.png")
        if self.id_block == 2:
            self.width = 16
            self.height = 32
            self.name = "attack_spider_warrior"
            self.image = pg.Surface((self.width, self.height))
            self.image = pg.image.load("data/texture/texture_attack/attack_spider_warrior.png")
        if self.id_block == 3:
            self.width = 16
            self.height = 16
            self.name = "attack_spider_archer"
            self.image = pg.Surface((self.width, self.height))
            self.image = pg.image.load("data/texture/texture_attack/attack_spider_archer.png")
        
        self.direction = direction
        
        if self.direction == 1:
            self.image = pg.transform.rotate(self.image, 180)
            self.rect = pg.Rect(x-16, y, self.width, self.height)
        elif self.direction == 2:
            self.rect = pg.Rect(x+32, y, self.width, self.height)
        elif self.direction == 3:
            self.image = pg.transform.rotate(self.image, 90)
            self.rect = pg.Rect(x-16, y-16, self.width, self.height)
        elif self.direction == 4:
            self.image = pg.transform.rotate(self.image, 270)
            self.rect = pg.Rect(x-16, y+64, self.width, self.height)
        self.speed = speed
        self.attack = attack
        self.time = time.time()
        self.duration = float(duration)

    def update(self, layer, base_interface):
        if time.time() - self.time >= self.duration:
            self.kill()
        if self.direction == 1:
            self.rect.x -= self.speed
        elif self.direction == 2:
            self.rect.x += self.speed
        elif self.direction == 3:
            self.rect.y -= self.speed
        elif self.direction == 4:
            self.rect.y += self.speed

        for obj in layer:
            if self.rect.colliderect(obj.rect):
                if obj.name == self.where:
                    pass
                else:
                    if obj.name != 'hero':
                        obj.heath -= self.attack
                        print(obj.name, obj.heath)
                    if obj.name == 'hero':
                        base_interface.heath -= self.attack

                    self.kill()
                    

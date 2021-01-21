import pygame as pg
import math
from attack_bullet import Attack_bullet
import time
import random


class Monster(pg.sprite.Sprite):
    def __init__(self, x, y, type_):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32, 32))
        self.name = 'monster'
        if type_ <= 2:
            self.name_2 = "monster_warrior"
            self.image = pg.image.load("data/texture/texture_monster/monster_warrior_left.png").convert()
            self.image_left = pg.image.load("data/texture/texture_monster/monster_warrior_left.png").convert()
            self.image_right = pg.image.load("data/texture/texture_monster/monster_warrior_right.png").convert()
            self.MOVE_SPEED = -(random.randint(5, 8)//2)
            self.radius = 100
            self.time_attack = 2.0
            self.heath = 50
            self.attack = 8
            self.duration = 0.8
        
        if type_ >= 3:
            self.name_2 = "monster_archer"
            self.image = pg.image.load("data/texture/texture_monster/monster_archer_left.png").convert()
            self.image_left = pg.image.load("data/texture/texture_monster/monster_archer_left.png").convert()
            self.image_right = pg.image.load("data/texture/texture_monster/monster_archer_right.png").convert()
            self.MOVE_SPEED = -(random.randint(1, 5)//2)
            self.radius = 150
            self.time_attack = 3.0
            self.heath = 25
            self.attack = 16
            self.duration = 4.0
        
        self.rect = pg.Rect(x, y, 32, 32)
        self.x = x // 32
        self.y = y // 32
        self.light_status = False
        self.direction = 0
        self.surf2 = pg.Surface((64, 64))
        self.surf2.fill((255, 255, 255))  # белая
        self.rect_2 = pg.Rect(x+32, y-16, 64, 64)
        self.rect_3 = pg.Rect(x-16, y-32, 64, 64)
        self.rect_4 = pg.Rect(x-16, y+32, 64, 64)
        self.time = time.time()
        

    def update(self, player, layer_2, layer_bullet, wall):
        if self.heath <= 0:
            print('True')
            self.kill()
        else:
            if player.x!= self.x and player.y != self.y:
                dx, dy = self.rect.x - player.rect.x, self.rect.y - player.rect.y
                if dx != 0 or dy != 0:
                    dist = math.hypot(dx, dy)
                    if dist > 50 and dist < self.radius*2:
                        dx, dy = dx / dist, dy / dist
                        self.rect.x += dx * self.MOVE_SPEED
                        self.rect.y += dy * self.MOVE_SPEED
                        
                        self.rect_2.x = self.rect.x+32
                        self.rect_2.y = self.rect.y-16
                        self.rect_3.x = self.rect.x+16
                        self.rect_3.y = self.rect.y-32
                        self.rect_4.x = self.rect.x-16
                        self.rect_4.y = self.rect.y+32

                    if dist < self.radius :
                        if time.time() - self.time >= self.time_attack:
                            self.image = self.image_left
                            self.direction = 1
                            if self.rect_2.colliderect(player.rect):
                                self.direction = 2
                                self.image = self.image_right
                            if self.rect_3.colliderect(player.rect):
                                self.direction = 3
                                self.image = self.image_left
                            if self.rect_4.colliderect(player.rect):
                                self.direction = 4
                                self.image = self.image_right
                            self.shoot(layer_2, layer_bullet)
                            self.time = time.time()


    
    def shoot(self, layer_2, layer_bullet):
        if self.name_2 == 'monster_warrior':
            bullet = Attack_bullet(self.rect.x, self.rect.y, 2, self.direction, -self.MOVE_SPEED*1.5, self.attack, self.duration, 'monster')
        else:
            bullet = Attack_bullet(self.rect.x, self.rect.y, 3, self.direction, -self.MOVE_SPEED*2.5, self.attack, self.duration, 'monster')
        layer_2.add(bullet)
        layer_bullet.add(bullet)

    


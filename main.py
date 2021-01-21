import random
import pygame as pg
import create_the_map
import rooms
import time
import sqlite3
import math

from player import Player
from floor import Floor
from camera import Camera
from wall import Wall
from base_interface import Base_interface
from attack_bullet import Attack_bullet
from chest import Chest
from weapon import Weapon
from torch import Torch
from monster_spawn import Monster_spawn
from monster import Monster
from potion import Potion


def create_weapond(x, y, properties):
    item = Weapon(x, y, properties)
    layer_1.add(item)
    print(39)

def update_fps():
    fps = str(int(FPS.get_fps()))
    fps_text = font.render(fps, 1, pg.Color("coral"))
    return fps_text

def show_text():
    text = str('open the chest')
    text_render = font.render(fps, 1, pg.Color("coral"))
    return text_render

def generation_room(x_initial, y_initial, room):
    x = x_initial
    y = y_initial
    for i in range(len(room)):
        for j in range(len(room[0])):
            if room[i][j] == "f":
                pf = Floor(x, y, random.randint(0,5))
                layer_0.add(pf)
            if room[i][j] == "w":
                pf = Wall(x, y, 4)
                layer_1.add(pf)
            if room[i][j] == "d":
                pf = Wall(x, y, 1)
                layer_2.add(pf)
            if room[i][j] == "v":
                pf = Wall(x, y, 2)
                layer_2.add(pf)
            if room[i][j] == "x":
                pf = Wall(x, y, 0)
                layer_0.add(pf)
                wall.append(pf)
            if room[i][j] == "u":
                pf = Wall(x, y, 3)
                layer_1.add(pf)
                r = random.randint(0, 100)
                if r <= 5:
                    torch = Torch(x, y, 3)
                    layer_1.add(torch)
            if room[i][j] == "c":
                r = random.randint(3, 10)
                if r >= 5:
                    pf = Floor(x, y, 6)
                    layer_0.add(pf)
                    pf = Chest(x, y-6, random.randint(1, 2))
                    layer_1.add(pf)
                    chest.append(pf)
                else:
                    pf = Floor(x, y, 6)
                    layer_0.add(pf)
            if room[i][j] == "z":
                pf = Monster_spawn(x, y)
                layer_0.add(pf)
                r = random.randint(2, 5)
                for i in range(r):
                    x_ = random.randint(pf.rect.x-32, pf.rect.x+64)
                    y_ = random.randint(pf.rect.y-32, pf.rect.y+64)
                    pf = Monster(x_, y_, random.randint(1, 4))
                    layer_1.add(pf)
                    layer_monster.add(pf)
                    layer_all_monster_and_layer.add(pf)

            x += 32
        x = x_initial
        y += 32



def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2
    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы
    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы
    return pg.Rect(l, t, w, h)      

layer_0 = pg.sprite.Group()    
layer_1 = pg.sprite.Group()
layer_2 = pg.sprite.Group()
layer_3 = pg.sprite.Group()

layer_bullet = pg.sprite.Group()
layer_monster = pg.sprite.Group()

layer_all_monster_and_layer = pg.sprite.Group()

wall = []
chest = []
weapon_items = []
potion_items = []

MOVE_SPEED = 5

WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

BLOCK_WIDTH = 32
BLOCK_HEIGHT = 32

pg.init()
pg.font.init()
screen = pg.display.set_mode((DISPLAY), pg.RESIZABLE)
pg.display.set_caption("Undeground. Die or remember.")

bg = pg.Surface((WIN_WIDTH,WIN_HEIGHT))
bg.fill((0,0,0))

run = True
level = create_the_map.data
rooms = rooms.rooms
left = right = up = down = False
FPS = pg.time.Clock()
start_x = start_y = 0
x = 64
y = 64
for row in level:
    for col in row:
        if col != '0':
            room = rooms[col]
            room = room[0]
            generation_room(x,y,room)
        if col == 's':
            start_x, start_y = x+32*10, y+32*10
        x += 20 * 32
    x = 64
    y += 20 * 32

#total_level_width  = len(levels[0])* 64 # Высчитываем фактическую ширину уровня
#total_level_height = len(levels) * 64   # высоту

font = pg.font.Font(None, 30)

hero = Player(start_x, start_y, MOVE_SPEED)
layer_1.add(hero)
layer_all_monster_and_layer.add(hero)
radius = 6
total_level_width  = len(level[0]) * 40 * 32 * 2 # Высчитываем фактическую ширину уровня

total_level_height = len(level) * 40 * 32 * 2   # высоту

camera = Camera(camera_configure, total_level_width, total_level_height)
print(camera.state.x, camera.state.y)
'''
field_of_vision = Field_of_vision(camera.state.x, camera.state.y)
layer_3.add(field_of_vision)
'''

base_interface = Base_interface(camera.state.x, camera.state.y)
layer_3.add(base_interface)

t = time.time()

pause_font = pg.font.SysFont('Comic Sans MS', 30)
pause_text = pause_font.render('Pause', False, (255, 255, 255))

end_font = pg.font.SysFont('Comic Sans MS', 30)
end_text = end_font.render('Game Over', False, (255, 255, 255))

event_e = False
pause = False
for obj in layer_1:
    if obj.name == 'torch':
        obj.updated(layer_0, layer_1, layer_2)

while run:
    FPS.tick(60)
    for e in pg.event.get():
        if e.type == pg.QUIT:
            run = False

        while base_interface.heath <= 0:
            for e in pg.event.get():
                if e.type == pg.QUIT:
                    run = False
                    pause = False
                    base_interface.heath = 1
                screen.blit(end_text, (370, 0))
                pg.display.flip()
        
        if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
            pause = True
            hero.image = hero.image_kill
            while pause:
                for e in pg.event.get():
                    if e.type == pg.QUIT:
                        run = False
                        pause = False
                    if e.type == pg.KEYDOWN and e.key == pg.K_ESCAPE:
                        pause = False
                    screen.blit(pause_text, (370, 0))
                    pg.display.flip()
        if e.type == pg.MOUSEBUTTONDOWN:
            if e.button == 1:
                if hero.weapon_1 != '':
                    if hero.weapon_type_1 == 'sword':
                        pf = Attack_bullet(hero.rect.x, hero.rect.y, 1, hero.direction, hero.MOVE_SPEED*1.5, hero.weapon_attack_1, hero.duration_1, 'hero')
                        layer_2.add(pf)
                        layer_bullet.add(pf)
            if e.button == 2:
                if hero.weapon_2 != '':
                    if hero.weapon_type_1 == 'sword':
                        pf = Attack_bullet(hero.rect.x, hero.rect.y, 1, hero.direction, hero.MOVE_SPEED*1.5, hero.weapon_attack_2, hero.duration_2, 'hero')
                        layer_2.add(pf)
                        layer_bullet.add(pf)
                        

        if e.type == pg.KEYDOWN and e.key == pg.K_e:
            for obj in chest:
                if obj.status == 'close':
                    condition = hero.rect.colliderect(obj)
                    if condition:
                        item = obj.open()
                        if item[0][6] == 'sword':
                            pf = Weapon(hero.rect.x+16, hero.rect.y+96, item)
                            weapon_items.append(pf)
                            layer_0.add(pf)
                        if item[0][6] == 'potion':
                            pf = Potion(hero.rect.x+16, hero.rect.y+96, item)
                            potion_items.append(pf)
                            layer_0.add(pf)
        
        if e.type == pg.KEYDOWN and e.key == pg.K_4:
            for obj in weapon_items:
                if obj.type == 'sword':
                    condition = hero.rect.colliderect(obj)
                    if condition:
                        layer_0.remove(obj)
                        weapon_items.remove(obj)
                        if  base_interface.image_4:
                            pf = Weapon(hero.rect.x+16, hero.rect.y+64, base_interface.properies_4)
                            weapon_items.append(pf)
                            layer_0.add(pf)
                        base_interface.image_bronze_4 = obj.image
                        base_interface.image_4 = True
                        base_interface.properies_4 = obj.properties
                        hero.weapon_1 = 'sword'
                        hero.weapon_type_1 = 'sword'
                        hero.weapon_attack_1 = int(obj.properties[0][1])
                        break

        if e.type == pg.KEYDOWN and e.key == pg.K_5:
            for obj in weapon_items:
                if obj.type == 'sword':
                    condition = hero.rect.colliderect(obj)
                    if condition:
                        layer_0.remove(obj)
                        weapon_items.remove(obj)
                        if base_interface.image_5:
                            pf = Weapon(hero.rect.x+16, hero.rect.y+64, base_interface.properies_5)
                            weapon_items.append(pf)
                            layer_0.add(pf)
                        base_interface.image_bronze_5 = obj.image
                        base_interface.image_5 = True
                        base_interface.properies_5 = obj.properties
                        hero.weapon_2 = 'sword'
                        hero.weapon_type_2 = 'sword'
                        hero.weapon_attack_2 = int(obj.properties[0][1])
                        break

        if e.type == pg.KEYDOWN and e.key == pg.K_6:
            if base_interface.type_6 == None:
                for obj in potion_items:
                    condition = hero.rect.colliderect(obj)
                    if condition:
                        layer_0.remove(obj)
                        potion_items.remove(obj)
                        base_interface.image_holy_6 = obj.image
                        base_interface.type_6 = obj.type_potion
            else:
                if base_interface.type_6 == 'heath':
                    base_interface.heath += 25
                    base_interface.image_holy_6 = pg.image.load("data/texture/texture_weapon/none.png")
                    base_interface.type_6 = None
                if base_interface.type_6 == 'mana':
                    base_interface.magia += 25
                    base_interface.image_holy_6 = pg.image.load("data/texture/texture_weapon/none.png")
                    base_interface.type_6 = None

        if e.type == pg.KEYDOWN and e.key == pg.K_7:
            if base_interface.type_7 == None:
                for obj in potion_items:
                    condition = hero.rect.colliderect(obj)
                    if condition:
                        layer_0.remove(obj)
                        potion_items.remove(obj)
                        base_interface.image_holy_7 = obj.image
                        base_interface.type_7 = obj.type_potion
            else:
                if base_interface.type_7 == 'heath':
                    base_interface.heath += 25
                    base_interface.image_holy_7 = pg.image.load("data/texture/texture_weapon/none.png")
                    base_interface.type_7 = None
                if base_interface.type_7 == 'mana':
                    base_interface.magia += 25
                    base_interface.image_holy_7 = pg.image.load("data/texture/texture_weapon/none.png")
                    base_interface.type_7 = None
                    
                             
        if e.type == pg.KEYDOWN and e.key == pg.K_LEFT:
            left = True
        if e.type == pg.KEYDOWN and e.key == pg.K_RIGHT:
            right = True
        if e.type == pg.KEYDOWN and e.key == pg.K_UP:
            up = True
        if e.type == pg.KEYDOWN and e.key == pg.K_DOWN:
            down = True
        if e.type == pg.KEYDOWN and e.key == pg.K_n:
            print('minus')
            base_interface.heath -= 15
        if e.type == pg.KEYDOWN and e.key == pg.K_p:
            print('plus')
            base_interface.heath += 15

        if e.type == pg.KEYUP and e.key == pg.K_RIGHT:
            right = False
        if e.type == pg.KEYUP and e.key == pg.K_LEFT:
            left = False
        if e.type == pg.KEYUP and e.key == pg.K_UP:
            up = False
        if e.type == pg.KEYUP and e.key == pg.K_DOWN:
            down = False
    
    screen.fill((0,0, 0))
    hero.update(left, right, up, down, wall) # передвижение
    camera.update(hero)
    layer_monster.update(hero, layer_2, layer_bullet, wall)
    layer_2.update(layer_all_monster_and_layer, base_interface)

    
    for e in layer_0:
        if -camera.state.x+radius*32 < e.rect.x and -camera.state.x + 800-radius*32-32 > e.rect.x and -camera.state.y+radius*32 < e.rect.y and -camera.state.y + 600-radius*32-32 > e.rect.y:
            screen.blit(e.image, camera.apply(e))
        elif e.light_status == True:
            screen.blit(e.image, camera.apply(e))

    for e in layer_1:
        if -camera.state.x+radius*32 < e.rect.x and -camera.state.x + 800-radius*32-32 > e.rect.x and -camera.state.y+radius*32 < e.rect.y and -camera.state.y + 600-radius*32-32 > e.rect.y:
            screen.blit(e.image, camera.apply(e))
        elif e.light_status == True:
            screen.blit(e.image, camera.apply(e))

    for e in layer_monster:
        if -camera.state.x+radius*32 < e.rect.x and -camera.state.x + 800-radius*32-32 > e.rect.x and -camera.state.y+radius*32 < e.rect.y and -camera.state.y + 600-radius*32-32 > e.rect.y:
            screen.blit(e.image, camera.apply(e))

    for e in layer_2:
        if -camera.state.x+radius*32 < e.rect.x and -camera.state.x + 800-radius*32-32 > e.rect.x and -camera.state.y+radius*32 < e.rect.y and -camera.state.y + 600-radius*32-32 > e.rect.y:
            screen.blit(e.image, camera.apply(e))

    layer_3.update(camera, screen)
    hero.collide_chest(chest, screen)
    hero.collide_weapon(weapon_items, screen)
    hero.collide_potion(potion_items, screen)

    for e in layer_3:
        screen.blit(e.image, camera.apply(e))

    fps = font.render(str(int(FPS.get_fps())), True, pg.Color('white'))
    screen.blit(fps, (758, 10))
    pg.display.flip()
    

pg.quit()


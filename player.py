import pygame as pg

MOVE_SPEED = 7
WIDTH = 32
HEIGHT = 64

class Player(pg.sprite.Sprite):
    def __init__(self, x, y, MOVE_SPEED):
        pg.sprite.Sprite.__init__(self)
        self.xvel = 0
        self.yvel = 0
        self.startX = x
        self.startY = y
        self.image = pg.Surface((WIDTH,HEIGHT))
        self.image = pg.image.load("data/texture/texture_player/player_stop_down.png")
        self.image_kill = pg.image.load("data/texture/texture_player/player_stop_kill.png")
        self.rect = pg.Rect(x, y, WIDTH, HEIGHT)
        self.MOVE_SPEED = MOVE_SPEED
        self.x = 0
        self.y = 0
        self.name = "hero"
        self.direction = [4, 0]
        self.heath = 99999

        self.weapon_1 = ''
        self.weapon_type_1 = ''
        self.weapon_attack_1 = 0
        self.duration_1 = 1.0
        
        self.weapon_2 = ''
        self.weapon_type_2 = ''
        self.weapon_attack_2 = 0
        self.duration_2 = 1.0

    def update(self,  left, right, up, down, wall):
        self.xvel = 0
        self.yvel = 0
        if left:
            self.xvel = int(-self.MOVE_SPEED)
            self.direction = 1
 
        if right:
            self.xvel = int(self.MOVE_SPEED)
            self.direction = 2

        if up:
            self.yvel = int(-self.MOVE_SPEED)
            self.image = pg.image.load("data/texture/texture_player/player_stop_up.png")
            self.direction = 3
 
        if down:
            self.yvel = int(self.MOVE_SPEED)
            self.image = pg.image.load("data/texture/texture_player/player_stop_down.png")
            self.direction = 4
        
        
        self.rect.y += self.yvel
        self.collide(0, self.yvel, wall)
        self.rect.x += self.xvel
        self.collide(self.xvel, 0, wall)
   
    def collide(self, xvel, yvel, wall):
        for p in wall:
            if pg.sprite.collide_rect(self, p): # если есть пересечение платформы с игроком

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.yvel = 0                 # и энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # и энергия прыжка пропадае

    def collide_chest(self, chest, screen):
        for obj in chest:
            if obj.status == 'close':
                condition = self.rect.colliderect(obj)
                if condition:
                    myfont = pg.font.SysFont('Comic Sans MS', 14)
                    textsurface = myfont.render('open the chest?', False, (255, 255, 255))
                    screen.blit(textsurface,(400,500))

    def collide_weapon(self, weapon, screen):
        for obj in weapon:
            condition = self.rect.colliderect(obj)
            if condition:
                myfont = pg.font.SysFont('Comic Sans MS', 14)
                textsurface = myfont.render('take a weapon?', False, (255, 255, 255))
                screen.blit(textsurface,(400,500))

    def collide_potion(self, weapon, screen):
        for obj in weapon:
            condition = self.rect.colliderect(obj)
            if condition:
                myfont = pg.font.SysFont('Comic Sans MS', 14)
                textsurface = myfont.render('take a potion?', False, (255, 255, 255))
                screen.blit(textsurface,(400,500))
                

import pygame

class Floor(pygame.sprite.Sprite):
    def __init__(self, x, y, id_block):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        if id_block == 'f':
            self.image = pygame.image.load("data/texture/texture_floor/floor_1.png")
            self.name = "floor_1"
        if id_block == 'c':
            self.image = pygame.image.load("data/texture/texture_floor/floor_chest.png")
            self.name = "floor_chest"
        self.rect = pygame.Rect(x*32, y*32, 32, 32)
        self.x = x
        self.y = y

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, id_block):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32, 32))
        self.id_block = id_block
        if id_block == 'x':
            self.name = "wall_none"
            self.image = pygame.image.load("data/texture/texture_wall/wall_none.png").convert()
            self.rect = pygame.Rect(x*32, y*32, 32, 32)
        if id_block == 'u':
            self.name = "wall_up_1"
            self.image = pygame.image.load("data/texture/texture_wall/wall_up_1.png").convert()
            self.rect = pygame.Rect(x*32, y*32, 32, 32)
        if id_block == 'w':
            self.name = "wall_up_2"
            self.image = pygame.image.load("data/texture/texture_wall/wall_up_2.png").convert()
            self.rect = pygame.Rect(x*32, y*32, 32, 32)
        if id_block == 'd':
            self.name = "wall_down_1"
            self.image = pygame.image.load("data/texture/texture_wall/wall_down_1.png").convert()
            self.rect = pygame.Rect(x*32, y*32, 32, 32)
        if id_block == 'v':
            self.name = "wall_down_2"
            self.image = pygame.image.load("data/texture/texture_wall/wall_down_2.png").convert()
            self.rect = pygame.Rect(x*32, y*32, 32, 32)
            
        self.x = x
        self.y = y



#Объявляем переменные
WIN_WIDTH = 800 #Ширина создаваемого окна
WIN_HEIGHT = 700 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную
rect = 20
x = y = 0
data = [['0' for i in range(rect)] for j in range(rect)]
all_sprite = pygame.sprite.Group()
cursor = ''
pygame.init() # Инициация PyGame, обязательная строчка
screen = pygame.display.set_mode(DISPLAY) # Создаем окошко
pygame.display.set_caption("create_room") # Пишем в шапку
bg = pygame.Surface((WIN_WIDTH,WIN_HEIGHT)) # Создание видимой поверхности
                                         # будем использовать как фон
bg.fill((0,0,0))     # Заливаем поверхность сплошным цветом
run = True
x = y = 0


while run: # Основной цикл программы
    for e in pygame.event.get(): # Обрабатываем события
        if e.type == pygame.QUIT:
            run = False
        if e.type == pygame.KEYDOWN:
             if e.key == pygame.K_w:
                cursor = 'w'
                print('w')
             if e.key == pygame.K_x:
                cursor = 'x'
                print('x')
             if e.key == pygame.K_f:
                cursor = 'f'
                print('f')
             if e.key == pygame.K_u:
                cursor = 'u'
                print('u')
             if e.key == pygame.K_d:
                cursor = 'd'
                print('d')
             if e.key == pygame.K_v:
                cursor = 'v'
                print('v')
             if e.key == pygame.K_c:
                cursor = 'c'
                print('c')
        if e.type == pygame.MOUSEBUTTONDOWN:
            if e.button == 1:
                pos = pygame.mouse.get_pos()
                if pos[0]//32*32 <= rect*32-32 and pos[1]//32*32 <= rect*32-32:
                    x = pos[0]//32
                    y = pos[1]//32
                    print(True, x, y)
                    if cursor == 'd':
                        data[y][x] = cursor
                        pf = Wall(x, y, 'd')
                        all_sprite.add(pf)
                    if cursor == 'v':
                        data[y][x] = cursor
                        pf = Wall(x, y, 'v')
                        all_sprite.add(pf)
                    if cursor == 'u':
                        data[y][x] = cursor
                        pf = Wall(x, y, 'u')
                        all_sprite.add(pf)
                    if cursor == 'w':
                        data[y][x] = cursor
                        pf = Wall(x, y, 'w')
                        all_sprite.add(pf)
                    if cursor == 'x':
                        data[y][x] = cursor
                        pf = Wall(x, y, 'x')
                        all_sprite.add(pf)
                    if cursor == 'f':
                        data[y][x] = cursor
                        pf = Floor(x, y, 'f')
                        all_sprite.add(pf)
                    if cursor == 'c':
                        data[y][x] = cursor
                        pf = Floor(x, y, 'c')
                        all_sprite.add(pf)
            if e.button == 2:
                for row in data:
                    for col in row:
                        print(col, end='')
                    print(',', end='')
                    print()
            if e.button == 3:
                pos = pygame.mouse.get_pos()
                x = pos[0]//32
                y = pos[1]//32
                for obj in all_sprite:
                    if x == obj.x and y == obj.y:
                        all_sprite.remove(obj)
                        data[y][x] = '0'
    screen.fill((0,0,0))      # Каждую итерацию необходимо всё перерисовывать

    x = y = 0
    
    for i in range(rect):
        for j in range(rect):
            pygame.draw.rect(screen, (255,255,255), (x, y, 32, 32), 1)
            x += 32
        x = 0
        y += 32
    all_sprite.draw(screen)
    pygame.display.update()     # обновление и вывод всех изменений на экран
        

pygame.quit()

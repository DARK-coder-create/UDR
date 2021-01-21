import random

data = [['0' for i in range(20)] for j in range(20)]
room = 25
data[10][10] = 's'
col = 0
while col < room:
    for i in range(20):
        for j in range(20):
            if data[i][j] != '0':
                r = random.randint(0, 1)
                if r:
                    r = random.randint(1, 4)
                    if r == 1:
                        if data[i][j-1] != '1' and data[i-1][j-1] != '1' and data[i+1][j-1] != '1':
                            data[i][j-1] = '1'
                            col += 1
                    elif r == 2:
                        if data[i][j+1] != '1' and data[i-1][j+1] != '1' and data[i+1][j+1] != '1':
                            data[i][j+1] = '1'
                            col += 1
                    elif r == 3:
                        if data[i+1][j] != '1' and data[i+1][j-1] != '1' and data[i+1][j+1] != '1':
                            data[i+1][j] = '1'
                            col += 1
                    elif r == 4:
                        if data[i-1][j] != '1' and data[i-1][j-1] != '1' and data[i-1][j+1] != '1':
                            data[i-1][j] = '1'
                            col += 1


for i in range(20):
    for j in range(20):
        if data[i][j] == '1':
            if data[i][j+1] != '0' and data[i][j-1] != '0' and data[i-1][j] != '0' and data[i+1][j] != '0':
                if data[i][j] != 's':
                    data[i][j] = 'x'

            if data[i-1][j] != '0' and data[i+1][j] == '0' and data[i][j+1] == '0' and data[i][j-1] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'u'  
            
            if data[i+1][j] != '0' and data[i-1][j] == '0' and data[i][j+1] == '0' and data[i][j-1] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'd'

            if data[i+1][j] != '0' and data[i-1][j] == '0' and data[i][j+1] == '0' and data[i][j-1] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'd'

            if data[i][j-1] == '0' and data[i][j+1] != '0' and data[i+1][j] == '0' and data[i-1][j] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'r'

            if data[i][j+1] == '0' and data[i][j-1] != '0' and data[i+1][j] == '0' and data[i-1][j] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'p'

            if data[i][j-1] != '0' and data[i][j+1] != '0' and data[i+1][j] == '0' and data[i-1][j] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'z'

            if data[i][j-1] == '0' and data[i][j+1] == '0' and data[i+1][j] != '0' and data[i-1][j] != '0':
                if data[i][j] != 's':
                    data[i][j] = 'f'

            if data[i][j-1] != '0' and data[i+1][j] != '0'and data[i][j+1] == '0' and data[i-1][j] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'v'

            if data[i][j-1] != '0' and data[i-1][j] != '0'and data[i][j+1] == '0' and data[i+1][j] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'h'

            if data[i][j+1] != '0' and data[i+1][j] != '0' and data[i-1][j] == '0' and data[i][j-1] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'j'

            if data[i][j+1] != '0' and data[i-1][j] != '0' and data[i+1][j] == '0' and data[i][j-1] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'k'

            if data[i][j-1] != '0' and data[i][j+1] != '0' and data[i-1][j] != '0' and data[i+1][j] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'm'

            if data[i][j-1] != '0' and data[i][j+1] != '0' and data[i+1][j] != '0' and data[i-1][j] == '0':
                if data[i][j] != 's':
                    data[i][j] = 'n'

            if data[i][j-1] != '0' and data[i][j+1] == '0' and data[i+1][j] != '0' and data[i-1][j] != '0':
                if data[i][j] != 's':
                    data[i][j] = 'a'

            if data[i][j-1] == '0' and data[i][j+1] != '0' and data[i+1][j] != '0' and data[i-1][j] != '0':
                if data[i][j] != 's':
                    data[i][j] = 'c'
data[10][10] = 's'


for row in data:
    for col in row:
        print(col, end="")
    print()

"""
0 - пустота
x - комната(4 двери)

u - тупик(с 1 дверью вверх)
d - тупик(с 1 дверью вниз)
p - тупик(с 1 дверью влево)
r - тупик(с 1 дверью вправо)

z - комната/коридор (горизонтальный)
f - комната/коридор (вертикальный)

v - комната (с дверью слева и снизу)
h - комната (с дверью слева и сверху)

j - комната (с дверь справа и снизу)
k - комната (с дверь справа и сверху)

m - комната (с дверь слева справа вверх)
n - комната (с дверь слева справа вниз)

a - комната (с дверь слева вверх вниз)
c - комната (с дверь справа вверх вниз)

"""

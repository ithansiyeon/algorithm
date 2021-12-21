n = int(input())
stars = [[" " for _ in range(n)] for _ in range(n)]

def star_print(size,x,y):
    if size == 1:
        stars[x][y] = '*'
        return
    size = size // 3
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1: continue
            star_print(size,x+i*size,y+j*size)

star_print(n,0,0)

for s in stars:
    print(''.join(s))
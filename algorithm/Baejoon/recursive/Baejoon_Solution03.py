n = int(input())
stars = [[' ' for _ in range(n)] for _ in range(n)]
def recur(size,x,y):
    if size == 1:
        stars[x][y] = '*'
    else:
        next_size = size // 3
        for i in range(3):
            for j in range(3):
                if i == 1 and j == 1: continue
                recur(next_size,x+next_size*i,y+next_size*j)

recur(n,0,0)

for i in stars:
    print(''.join(i))

stars = [[' ' for _ in range(n)] for _ in range(n)]


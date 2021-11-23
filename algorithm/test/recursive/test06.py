n = int(input())
square = []
result = [0]*2
for i in range(n):
    square.append(list(map(int,input().split(" "))))

def recur(x,y,size):
    sum = 0
    loop = True
    for i in range(x,x+size):
        for j in range(y,y+size):
            sum+=square[i][j]
    if sum == 0:
        result[0] += 1
        loop = False
    elif sum == size ** 2:
        result[1] += 1
        loop = False
    if loop:
        print(size)
        if sum != size**2 or sum != 0:
            size=size//2
            recur(x,y,size)
            recur(x,y+size,size)
            recur(x+size,y,size)
            recur(x+size,y+size,size)

    return result

for i in recur(0,0,n):
    print(i)
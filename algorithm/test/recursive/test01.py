n = int(input())
video = []
result = ""
for i in range(n):
    video.append(list(input()))

def div(x,y,size):
    global result
    loop = True
    check = video[x][y]
    for i in range(x,x+size):
        for j in range(y,y+size):
            if video[i][j]!=check:
                loop = False
                result += "("
                size //= 2
                div(x, y, size)
                div(x, y + size, size)
                div(x + size, y, size)
                div(x + size, y + size, size)
                result += ")"
                break
        if not loop:
            break
    if loop:
        result+=video[x][y]

    return result
print(div(0,0,n))



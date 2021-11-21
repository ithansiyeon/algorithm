n = int(input())
video = []
result = ""
for i in range(n):
    video.append(list(map(int,input())))

def div(x,y,size):
    global result
    hap = 0
    loop = True
    for i in range(x,x+size):
        for j in range(y,y+size):
            hap+=video[i][j]

    if hap == size*size:
        result+="1"
        loop = False
    elif hap == 0:
        result+="0"
        loop = False
    elif size==2:
         result += "("
         result+=str(video[x][y]) + str(video[x][y+1]) + str(video[x + 1][y]) + str(video[x + 1][y+1])
         result += ")"

    if loop and size!=2:
        result += "("
        size //= 2
        div(x,y,size)
        div(x,y+size,size)
        div(x+size,y,size)
        div(x+size,y+size,size)
        result += ")"

    return result
print(div(0,0,n))



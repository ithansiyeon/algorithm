n = int(input())
paper = []
sum = [0]*3
for i in range(n):
    paper.append(list(map(str,(input().split(" ")))))

def div_count(x,y,size):
    cnt0 = 0
    cnt1 = 0
    cnt2 = 0
    loop = True
    for i in range(x,x+size):
        for j in range(y,y+size):
            if paper[i][j] == '1':
                cnt1+=1
            elif paper[i][j] == '0':
                cnt0+=1
            else:
                cnt2+=1
    m = size*size

    if cnt1==m:
        sum[2]+=1
        loop = False
    elif cnt2==m:
        sum[0]+=1
        loop = False
    elif cnt0==m:
         sum[1]+=1
         loop = False

    if cnt1 != m and cnt0 != m and cnt2 != m and size==3:
        sum[0] += cnt2
        sum[1] += cnt0
        sum[2] += cnt1
        loop = False

    if loop:
        size=size//3
        div_count(x,y,size)
        div_count(x,y+size,size)
        div_count(x, y + size*2, size)
        div_count(x+size,y,size)
        div_count(x+size,y+size,size)
        div_count(x + size, y + size*2, size)
        div_count(x+size*2,y,size)
        div_count(x + size * 2, y+size, size)
        div_count(x + size * 2, y+size*2, size)
    return sum
for i in div_count(0,0,n):
    print(i)



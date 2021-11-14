n = int(input())
direct = list(input().split(" "))
# R L D U
dx = [0,0,1,-1]
dy = [1,-1,0,0]
x,y = 1,1
directs = {'R':(0,1),'L':(0,-1),'D':(1,0),'U':(-1,0)}
for d in direct:
    if directs[d][1]+y < 1 or directs[d][1]+y > 5 or directs[d][0]+x < 1 or directs[d][0]+x > 5:
        continue
    else:
        x+=directs[d][0]
        y+=directs[d][1]

print(x,y)

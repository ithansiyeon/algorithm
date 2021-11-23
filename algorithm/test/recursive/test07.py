import sys

n,r,c = map(int,input().split(" "))
cnt = 0
def recur(x,y,size):
    global cnt
    if size == 2:
        if x == r and y == c:
            print(cnt)
            sys.exit(0)
        if x == r and y+1 == c:
            print(cnt+1)
            sys.exit(0)
        if x+1 == r and y == c:
            print(cnt+2)
            sys.exit(0)
        if x+1 == r and y+1 == c:
            print(cnt+3)
            sys.exit(0)
        cnt+=4
    else:
        if r <= x+size//2 and c <= y+size//2:
            recur(x,y,size//2)
        else:
            cnt+=(size//2)**2
        if r <= x+size//2 and c <= y + size//2*2:
             recur(x,y+size//2,size//2)
        else:
            cnt+=(size//2)**2
        if r <= x+size//2*2 and c <= y+size//2:
            recur(x+size//2,y,size//2)
        else:
            cnt += (size // 2) ** 2
        if r <= x+size//2*2 and c <= y+size//2*2:
            recur(x+size//2,y+size//2,size//2)
        else:
            cnt += (size // 2) ** 2
print(recur(0,0,2**n))
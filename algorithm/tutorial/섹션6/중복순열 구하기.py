import sys

sys.stdin = open("in5.txt", "rt")

n,m = map(int,input().split())

def dfs(l):
    global cnt
    if l == m:
        cnt+=1
        for i in range(m):
            print(res[i],end=" ")
        print()
        return
    for i in range(1,n+1):
        res[l] = i
        dfs(l+1)


if __name__ == '__main__':
    res = [0]*m
    cnt =0
    dfs(0)
    print(cnt)
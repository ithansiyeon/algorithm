import sys

sys.stdin = open("in5.txt", "rt")

def dfs(l,sum,tsum):
    global res
    if sum > c:
        return
    if sum + total-tsum < res:
        return
    if l == n:
        res = max(res,sum)
    else:
        dfs(l+1,sum+dogs[l],tsum+dogs[l])
        dfs(l+1,sum,tsum+dogs[l])


if __name__ == '__main__':
    c, n = map(int, input().split())
    dogs = [int(input()) for i in range(n)]
    res = -10000
    total = sum(dogs)
    dfs(0,0,0)
    print(res)
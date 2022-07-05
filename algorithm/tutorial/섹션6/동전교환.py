import sys

sys.stdin = open("in5.txt", "rt")

def dfs(sum,cnt):
    global res
    if cnt >= res:
        return
    if sum > m:
        return
    if sum == m:
        res = min(res,cnt)
    else:
        for i in range(n):
            dfs(sum+money[i],cnt+1)

if __name__ == '__main__':
    n = int(input())
    money = list(map(int,input().split()))
    money.sort(reverse=True)
    m = int(input())
    res = 1000000000000000
    dfs(0,0)
    print(res)
import sys

sys.stdin = open("in5.txt", "rt")

def dfs(l,sum):
    if sum > hap // 2:
        return
    if sum == (hap-sum):
        print("YES")
        sys.exit(0)
    if l == n:
        return
    else:
        dfs(l+1,sum+nlist[l])
        dfs(l+1,sum)


if __name__ == '__main__':
    n = int(input())
    nlist = list(map(int, input().split()))
    hap = sum(nlist)
    dfs(0,0)
    print("NO")

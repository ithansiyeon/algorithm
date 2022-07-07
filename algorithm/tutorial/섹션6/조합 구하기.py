def dfs(l,val):
    global cnt
    if l == m:
        for i in range(m):
            print(res[i],end=" ")
        print()
        cnt+=1
    else:
        for i in range(val,n+1):
            res[i]=i
            dfs(l+1,res[l]+1)

if __name__ == '__main__':
    cnt = 0
    n,m = 8,3
    res = [0]*m
    dfs(0,1)
    print(cnt)
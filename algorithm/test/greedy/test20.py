n,m = map(int,input().split(" "))
weights = list(map(int,input().split(" ")))
cnt = 0
for i in range(n):
    for j in range(i,n):
        if weights[i] != weights[j]:
            cnt+=1
print(cnt)

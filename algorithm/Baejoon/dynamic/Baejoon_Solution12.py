n=int(input())
a=list(map(int,input().split()))
dl=[1]*1000
dr=[1]*1000
for i in range(n):
    for j in range(i):
        if a[i]>a[j]:
            dl[i]=max(dl[i],dl[j]+1)
for i in range(n-1,-1,-1):
    for j in range(n-1,i,-1):
        if a[i]>a[j]:
            dr[i]=max(dr[i],dr[j]+1)
MAX=-int(1e9)
for i in range(n):
    if dl[i]+dr[i]>MAX:
        MAX=dl[i]+dr[i]
print(MAX-1)
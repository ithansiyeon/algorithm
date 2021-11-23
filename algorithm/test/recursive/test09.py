n = int(input())
for i in range(n):
    k = int(input())
    n = int(input())
    plist = list(range(1,n+1))
    while k > 0:
        k-=1
        for i in range(1,n):
            plist[i]+=plist[i-1]
    print(plist[n-1])
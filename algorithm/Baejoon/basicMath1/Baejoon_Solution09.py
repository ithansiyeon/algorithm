n = int(input())
for i in range(n):
    a,b = map(int,input().split(" "))
    cnt = 1
    while a < b-1:
        a += a+1
        cnt+=1
        print(a)
    print(cnt)

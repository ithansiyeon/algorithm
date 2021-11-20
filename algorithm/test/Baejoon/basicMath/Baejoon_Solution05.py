num = int(input())
for i in range(num):
    h,w,n = map(int,input().split(" "))
    b = n % h
    if b == 0:
        b = h
    if n//h < n/h:
        a = n//h+1
    else:
        a = n//h

    print(str(b)+str(a).zfill(2))
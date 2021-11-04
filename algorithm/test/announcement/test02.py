a,b = map(int,input().split(" "))
min = a*60+b - 45
if min < 0:
    h = 23
    m = 60+min
else:
    h = min//60
    m = min%60
print(h,m)


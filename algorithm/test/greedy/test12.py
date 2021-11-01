a,b = map(int,input().split(" "))
balls = list(map(int,input().split(" ")))
cnt = 0
for i in range(a):
    for j in range(i+1,a):
        if balls[i] != balls[j]:
            cnt+=1
print(cnt)

array = [0]*11
for x in balls:
    array[x]+=1
print(array)
result = 0
for i in range(1,b+1):
    a-=array[i]
    result+=array[i]*a
print(result)
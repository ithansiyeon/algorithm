n = int(input())

data = list(input().split() for _ in range(n))
data.sort(key=lambda x:x[1])

for i in data:
    print(i[0],end=" ")
n = int(input())
data = []
for i in range(n):
    a,b = map(int,input().split(" "))
    data.append((b,a))

data.sort()

for i in data:
    print(i[1],i[0])
n = int(input())
data = []
for i in range(n):
    data.append(input().split(" "))

array = sorted(data,key=lambda data: data[1])

for student in array:
    print(student[0],end=' ')
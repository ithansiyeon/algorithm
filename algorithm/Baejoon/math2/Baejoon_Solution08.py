from collections import defaultdict

list1 = []
for i in range(3):
    list1.append([tuple(map(int,input().split()))])

dic = defaultdict(int)
dic1 = defaultdict(int)

for i in list1:
    dic[i[0][0]] += 1
    dic1[i[0][1]] += 1

x = 0

for key,value in dic.items():
    if value == 1:
        x = key
y = 0
for key,value in dic1.items():
    if value == 1:
        y = key
print(x,y)


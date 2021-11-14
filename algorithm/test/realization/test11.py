from itertools import combinations
a,b = map(int,input().split(" "))
city = []
home = []
chick = []
for i in range(a):
    city.append(list(map(int,input().split(" "))))
    for j in range(a):
        if city[i][j] == 1:
            home.append((i,j))
        elif city[i][j] == 2:
            chick.append((i,j))

pick_chick = list(combinations(chick,b))
result=[0]*len(pick_chick)
for i in home:
    sum = 0
    for j in range(len(pick_chick)):
      d = 1000
      for k in pick_chick[j]:
          temp = abs(i[0]-k[0])+abs(i[1]-k[1])
          d = min(d,temp)
      result[j]+=d
print(min(result))

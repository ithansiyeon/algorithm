n = int(input())
dis = list(map(int,input().split(" ")))
cost = list(map(int,input().split(" ")))
sum=cost[0]*dis[0]
min1 = cost[0]
for i in range(1,len(dis)):
    min1 = min(min1,cost[i])
    sum+=dis[i]*min1
print(sum)




import sys
sys.stdin = open("in2.txt", "rt")
n = int(input())
sqaure = []
for i in range(n):
    sqaure.append(list(map(int,input().split())))

m = int(input())

for i in range(m):
    r, d, k = map(int, input().split())
    if(d==0):
        for _ in range(k):
            sqaure[r-1].append(sqaure[r-1].pop(0))
    else:
        for _ in range(k):
            sqaure[r-1].insert(0, sqaure[r-1].pop())

a = 0
b = n
y = 0
hap = 0

while True:
   if y == n:
       break
   for i in range(a,b):
       print(sqaure[y][i])
       hap+=sqaure[y][i]
   y+=1
   if y <= n//2:
       a+=1
       b-=1
   else:
       a-=1
       b+=1

for l in sqaure:
    print(l)
print(hap)





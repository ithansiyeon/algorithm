import sys
sys.stdin = open("in5.txt", "rt")
n = int(input())
apple = []
for _ in range(n):
    apple.append(list(map(int,input().split())))

a = n // 2
b = n // 2
y = 0
hap = apple[y][a]
while True:
    y += 1
    if y == n:
        break
    if y > n//2:
        a+=1
        b-=1
    else:
        a-=1
        b+=1
    for i in range(a,b+1):
        hap += apple[y][i]

print(hap)

import sys
input = sys.stdin.readline
n,m = map(int,input().split())
data = list(map(int,input().split()))
result = 0
for i in range(n):
    for j in range(i+1,n):
        for k in range(j+1,n):
            s = data[i]+data[j]+data[k]
            if s <= m:
                result = max(result,s)
print(result)
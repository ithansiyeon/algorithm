import sys
sys.stdin = open("in5.txt", "rt")

n = int(input())
data = [list(map(int,input().split())) for _ in range(n)]
data.sort(key=lambda x:(x[1],x[0]))

cnt = 1
end = data[0][1]

for i in range(1,n):
    if end <= data[i][0]:
        cnt+=1
        end = data[i][1]

print(cnt)
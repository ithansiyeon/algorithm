from sys import stdin
n = int(stdin.readline())

lines = []

for _ in range(n):
    a, b = map(int, stdin.readline().split())
    lines.append((a, b))

lines.sort()
dp = [1 for i in range(n)]
# a 전깃줄 번호를 기준으로 오름차순 정렬된 b 전깃줄 번호의 수열
a_to_b = list(map(lambda x: x[1], lines))
for i in range(n):
    for j in range(i):
        if a_to_b[i]>a_to_b[j] and dp[i]<dp[j]+1:
            dp[i] = dp[j]+1
print(n-max(dp))


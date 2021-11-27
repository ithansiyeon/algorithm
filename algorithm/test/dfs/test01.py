n, m = map(int, input().split(" "))
frame = []

for i in range(n):
    frame.append(list(map(int, input())))


def dfs(a, b):
    if a <= -1 or a >= n or b <= -1 or b >= m:
        return False
    if frame[a][b] == 0:
        frame[a][b] = 1
        dfs(a - 1, b)
        dfs(a + 1, b)
        dfs(a, b - 1)
        dfs(a, b + 1)
        return True
    return False


cnt = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            cnt += 1

print(cnt)

from sys import stdin
n = int(stdin.readline())
lines = []
for i in range(n):
    a, b = map(int, stdin.readline().split())
    lines.append((a, b))
lines.sort()
a_to_b = list(map(lambda x: x[1], lines))
dp = [a_to_b[0]]

    

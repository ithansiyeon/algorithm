import sys

n = int(sys.stdin.readline().rstrip())
stack = []
for i in range(n):
    stack.append(int(sys.stdin.readline().rstrip()))

cnt = 1
max = stack.pop()
while stack:
    a = stack.pop()
    if a > max:
        max = a
        cnt+=1

print(cnt)
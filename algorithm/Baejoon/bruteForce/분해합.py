import sys
n = int(sys.stdin.readline())
answer = []
for i in range(1,n):
    s = i
    for j in str(i):
        s+=int(j)
    if s == n:
        answer.append(i)
if len(answer) == 0:
    print(0)
else: print(min(answer))
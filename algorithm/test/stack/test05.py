import sys
n = int(sys.stdin.readline().rstrip())
stack = []
cur = 1
result = []
for i in range(n):
    num = int(sys.stdin.readline().rstrip())
    while cur <= num:
        stack.append(cur)
        cur+=1
        result.append("+")
    if stack[-1] == num:
        stack.pop()
        result.append("-")

if len(stack) != 0:
    print("NO")
else:
    print("\n".join(result))
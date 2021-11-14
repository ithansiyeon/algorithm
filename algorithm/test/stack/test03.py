import sys

n = int(input())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    stack = []
    loop = False
    for j in s:
        if j == "(":
            stack.append(j)
        else:
            if len(stack) == 0:
                loop = True
                break
            stack.pop()
    if len(stack) == 0 and not loop:
        print("YES")
    elif len(stack) != 0 or loop:
        print("NO")

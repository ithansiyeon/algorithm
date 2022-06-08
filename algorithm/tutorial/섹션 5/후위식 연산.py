import sys

sys.stdin = open("in5.txt", "rt")
data = input()
stack = []
result = 0
for d in data:
    if d.isdigit():
        stack.append(d)
    else:
        x = stack.pop()
        y = stack.pop()
        stack.append(str(eval(y+d+x)))

print(stack[0])
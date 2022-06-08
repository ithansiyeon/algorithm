import sys

sys.stdin = open("in1.txt", "rt")
a,b = map(int,input().split())
a = list(map(int,str(a)))

stack = []

for x in a:
    # 앞의 자료가 나보다 작으면 지워주고 전진을 해
    while stack and b > 0 and stack[-1] < x:
        stack.pop()
        b-=1
    stack.append(x)

if b!=0:
    stack = stack[:-b]

stack = ''.join(map(str,stack))
print(stack)


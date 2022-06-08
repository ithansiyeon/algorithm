import sys

sys.stdin = open("in5.txt", "rt")
data = list(map(str,input()))
stack = []
res = 0
for i in range(len(data)):
    if data[i] == "(":
        stack.append("(")
    elif data[i] == ")" and data[i-1] == "(":
        stack.pop()
        res+=len(stack)
    elif data[i] == ")":
        stack.pop()
        res+=1

print(res)



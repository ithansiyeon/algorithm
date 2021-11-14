import sys
n = int(sys.stdin.readline().rstrip())
nlist = list(map(int,sys.stdin.readline().rstrip().split(" ")))
result = ['-1']*n
stack = []
stack.append(0)
i = 1
while stack and i<n:
    while stack and nlist[stack[-1]] < nlist[i]:
        result[stack[-1]] = str(nlist[i])
        stack.pop()
    stack.append(i)
    i+=1

print(" ".join(result))

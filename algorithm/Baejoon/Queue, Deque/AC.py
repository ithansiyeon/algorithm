import ast
import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for i in range(t):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline().rstrip())
    nlist = deque(sys.stdin.readline().rstrip()[1:-1].split(","))
    flag = 0
    if n == 0:
        nlist = []
    for j in p:
        if j == "R":
            flag+=1
        elif j == "D":
            if len(nlist) == 0:
                print("error")
                break
            else:
                if flag % 2 == 0:
                    nlist.popleft()
                else:
                    nlist.pop()
    else:
        if flag % 2 == 0:
            print("[" + ",".join(nlist) + "]")
        else:
            nlist.reverse()
            print("[" + ",".join(nlist) + "]")


import sys

sys.stdin = open("in5.txt", "rt")
a1 = list(map(str,input()))
a2 = list(map(str,input()))

a1.sort()
a2.sort()

if "".join(a1) == "".join(a2):
    print("YES")
else:
    print("NO")
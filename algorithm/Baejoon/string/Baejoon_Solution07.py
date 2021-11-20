import sys
s = list(sys.stdin.readline().rstrip())
s.reverse()
a,b = map(int,"".join(s).split(" "))
if a > b:
    print(a)
else:
    print(b)
import sys

string = sys.stdin.readline().rstrip().strip()
if len(string) == 0:
    print(0)
else:
    print(len(string.split(" ")))


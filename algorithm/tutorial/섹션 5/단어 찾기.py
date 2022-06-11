import sys

sys.stdin = open("in5.txt", "rt")
n = int(input())
nlist = set([input() for _ in range(n)])
poem = set([input() for _ in range(n-1)])
print(list(nlist-poem)[0])
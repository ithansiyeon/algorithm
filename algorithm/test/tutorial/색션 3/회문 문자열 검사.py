import sys
sys.stdin = open("in1.txt", "rt")
n = int(input())

for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("YES")
    else:
        print("NO")
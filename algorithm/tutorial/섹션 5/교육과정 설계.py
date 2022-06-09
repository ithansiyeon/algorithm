import sys

sys.stdin = open("in5.txt", "rt")
data = list(map(str,input()))
n = int(input())

for i in range(n):
    subj = list(map(str,input()))
    res = []
    while subj:
        d = subj.pop(0)
        if d in data:
            res.append(d)
    if res == data:
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))




import math
import sys
sys.stdin = open("in5.txt", "rt")
string = input()

loop = True
s = ""
cnt = 0
for i in string:
    if i >= '0' and i <= '9':
        if i == '0' and len(s) == 0:
            pass
        else:
            s+=i

s = int(s)
for i in range(1,int(math.sqrt(s))+1):
    if s % i == 0:
        cnt +=1

print(s)
print(cnt*2)

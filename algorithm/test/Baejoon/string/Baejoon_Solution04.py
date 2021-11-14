from sys import stdin
n = int(stdin.readline())
for i in range(n):
    a,b = stdin.readline().split()
    result = ""
    for j in range(len(b)):
        result+=b[j]*int(a)
    print(result)



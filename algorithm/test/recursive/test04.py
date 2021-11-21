import sys
n = sys.stdin.readline().rstrip()
cnt = 0
def check(n):
    global cnt
    if len(n) > 1:
        sum = 0
        cnt+=1
        for i in n:
            sum+=int(i)
        check(str(sum))
    else:
        if int(n) % 3 == 0:
            print(cnt)
            print("YES")
        else:
            print(cnt)
            print("NO")

check(n)

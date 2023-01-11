t = int(input())

alist = [input() for _ in range(t)]

cnt = 1

def recursion(s,l,r):
    global cnt
    if l>=r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        cnt+=1
        return recursion(s,l+1,r-1)

for i in range(t):
    print(recursion(alist[i],0,len(alist[i])-1), cnt)
    cnt = 1

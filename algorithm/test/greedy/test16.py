import sys
for i in range(int(input())):
    list1 = []
    n = int(input())
    for i in range(n):
        a,b = map(int,sys.stdin.readline().strip().split())
        list1.append([a,b])
    list1.sort()
    cnt = 1
    min = list1[0][1]
    for i in range(1,n):
        if list1[i][1] < min:
            min = list1[i][1]
            cnt+=1
    print(cnt)

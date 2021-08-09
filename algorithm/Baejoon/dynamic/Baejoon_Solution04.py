m = [1, 1, 1, 2, 2] + [0] * 100
for i in range(int(input())):
    n = int(input())
    cnt = 5
    if m[n-1] == 0:
        while cnt!=n:
            m[cnt] = m[cnt-3] + m[cnt-2]
            cnt+=1
        print(m[n-1])
    else:
        print(m[n-1])


t = int(input())

for i in range(t):
    n,m = map(int,input().split(" "))
    a = list(map(int,input().split(" ")))
    array = [a[i:i+m] for i in range(0,n*m,m)]

    for j in range(1,m):
        for k in range(n):
            up,down = 0,0
            if k + 1 < n:
                down = array[k+1][j-1]
            if k - 1 >= 0:
                up = array[k-1][j-1]

            array[k][j]+=max(down,up,array[k][j-1])

    answer = 0

    for j in range(n):
        answer = max(answer,array[j][-1])
    print(answer)


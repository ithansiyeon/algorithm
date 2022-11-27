# N*M크기의 두 행렬 A와 B가 주어졌을 때, 두 행렬을 더하는 프로그램을 작성하시오.

n,m = map(int,input().split(" "))

A = []
for i in range(n):
    A.append([0])
    for j in range(m-1):
        A[i]+=[0]

i = 0
cnt = 0
while True:
    arr = list(map(int,input().split(" ")))
    for j in range(m):
        A[i][j] += arr[j]
    i+=1
    if i == n:
        i = 0
        cnt+=1
        if cnt == 2:
            break

for i in range(n):
    for j in range(m):
        print(A[i][j],end=" ")
    print()
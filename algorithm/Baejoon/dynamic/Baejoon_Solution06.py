triangle = []
for i in range(int(input())):
    triangle.append(list(map(int,input().split())))
triangle = [[0] + line + [0] for line in triangle]
for i in range(1,len(triangle)):
    for j in range(1,i+2):
        triangle[i][j]+=max(triangle[i-1][j-1],triangle[i-1][j])
print(max(triangle[-1]))

import sys
input = sys.stdin.readline
n,m = map(int,input().split())

array = []
for i in range(n):
    array.append(list(input().rstrip()))

answer = 0

def black(sub_array):
    cnt = 0
    for j in range(8):
        for k in range(8):
            if (j+k) % 2 == 0:
                if sub_array[j][k] != 'B':
                    cnt+=1
            else:
                if sub_array[j][k] != 'W':
                    cnt+=1
    return cnt

def white(sub_array):
    cnt = 0
    for j in range(8):
        for k in range(8):
            if (j+k) % 2 == 0:
                if sub_array[j][k] != 'W':
                    cnt+=1
            else:
                if sub_array[j][k] != 'B':
                    cnt+=1
    return cnt

val = int(1e9)
for i in range(n-7):
    for j in range(m-7):
        sub_array = [row[j:j+8] for row in array[i:i+8]]
        val = min(white(sub_array),black(sub_array),val)

print(val)

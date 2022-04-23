import sys
sys.stdin = open("in2.txt", "rt")
a = [list(map(int,input().split())) for _ in range(9)]

x = 0
y = 0
cnt = 0
cnt1 = 1
while True:
    cnt1+=1
    nums = set()
    if x == 9:
        break
    for i in range(x,x+3):
        for j in range(y,y+3):
            nums.add(a[i][j])
    if len(nums) == 9:
        cnt+=1
    if y == 6:
        y = 0
    else:
        y += 3
    if cnt1 % 3 == 1:
        x+=3
print("YES" if cnt == 9 else "NO")




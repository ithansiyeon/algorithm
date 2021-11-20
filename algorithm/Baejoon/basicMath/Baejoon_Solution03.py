n = int(input())
sum = 1
cnt = 2
while sum < n:
    sum+=cnt
    cnt+=1

if cnt%2 == 0:
    print('{}/{}'.format(sum-(n-1),cnt-(sum-(n-1))))
else:
    print('{}/{}'.format(cnt-(sum-(n-1)),sum-(n-1)))

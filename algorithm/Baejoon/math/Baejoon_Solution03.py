n = int(input())
cnt = 0
loop = True
sum = 0
add = 1
while sum < n:
    sum+=add
    add+=1
add-=1
sum-=add
cnt=sum

if add % 2 == 0:
    i = n - sum
    j = add - i +1
else:
    i = add - (n - sum) + 1
    j = n - sum
print(f'{i}/{j}')

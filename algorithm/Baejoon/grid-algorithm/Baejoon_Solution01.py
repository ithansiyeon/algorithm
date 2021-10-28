n,k = map(int, input().split(" "))
coin_type = []
for i in range(n):
    coin_type.append(int(input()))
coin_type.sort(reverse=True)
cnt = 0
while k>0:
    for coin in coin_type:
        if k >= coin:
            cnt += k // coin
            k = k % coin

print(cnt)
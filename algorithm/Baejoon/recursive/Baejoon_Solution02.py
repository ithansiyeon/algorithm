n = int(input())
dp = [0]*(n+1)
def fibo(x):
    if x == 1:
        return 1
    elif x == 0:
        return 0
    if dp[x] != 0:
        return dp[x]
    else:
        dp[x] = fibo(x-1) + fibo(x-2)
        return dp[x]

print(fibo(n))




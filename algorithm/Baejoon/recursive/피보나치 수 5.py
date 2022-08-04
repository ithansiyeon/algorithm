n = int(input())
dp = [0 for _ in range(n+1)]

def pibo(n):
    if n == 0:
        return dp[0]
    elif n == 1:
        dp[1] = 1
        return dp[1]
    if dp[n] != 0:
        return dp[n]
    else:
        dp[n] = pibo(n-1) + pibo(n-2)
        return dp[n]

print(pibo(n))

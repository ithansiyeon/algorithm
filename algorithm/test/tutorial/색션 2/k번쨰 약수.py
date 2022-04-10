import sys

# sys.stdin = open("input.txt","rt")
n,k = map(int,input().split())

primes = []
for i in range(1,n+1):
    if n % i == 0:
        primes.append(i)

primes.sort()

try:
    print(primes[k-1])
except:
    print(-1)

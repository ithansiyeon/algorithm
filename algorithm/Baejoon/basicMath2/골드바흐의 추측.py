t = int(input())
nlist = []
for i in range(t):
    nlist.append(int(input()))

m = max(nlist)
prime = [True for i in range(m+2)]

for i in range(2,m):
    if prime[i]:
        for j in range(i*2,m+1,i):
            prime[j] = False

for i in nlist:
    val = 1000000
    result = [0]*2
    for j in range(2,i+1):
        if prime[j] and prime[i-j]:
            if val > abs(i-2*j):
                result[0] = j
                result[1] = i-j
                val = abs(i-2*j)
    print(" ".join(map(str,sorted(result))))







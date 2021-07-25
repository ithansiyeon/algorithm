import copy

a = [False, False] + [True] * (10000 - 1)
primes = []
for i in range(2, 10000 + 1):
    if a[i]:
        primes.append(i)
        for j in range(2 * i, 10000 + 1, i):
            a[j] = False

for i in range(int(input())):
    dic = {}
    n = int(input())
    n1 = copy.deepcopy(n)
    for j in range(n+1):
        if a[j]:
            n1 -= j
            if a[n1]:
                if j > n1:
                    dic[j-n1] = f'{n1} {j}'
                else:
                    dic[n1-j] = f'{j} {n1}'
                n1 = copy.deepcopy(n)
            else:
                n1 = copy.deepcopy(n)
    print(dic[min(dic.keys())])

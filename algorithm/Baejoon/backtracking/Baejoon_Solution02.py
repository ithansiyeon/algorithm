import itertools
n,m = map(int,input().split())
n = [str(x) for x in range(1,n+1)]
for i in list(itertools.combinations(n,m)):
    print(' '.join(i))
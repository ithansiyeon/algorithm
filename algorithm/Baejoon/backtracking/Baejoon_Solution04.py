import itertools
n,m = map(int,input().split())
n1 = [str(x) for x in range(1,n+1)]
for i in itertools.combinations_with_replacement(n1,m):
    print(' '.join(list(i)))

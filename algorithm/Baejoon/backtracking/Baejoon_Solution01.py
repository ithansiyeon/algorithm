import itertools
n,m = map(int,input().split())
n1 = [str(x) for x in range(1,n+1)]
permute = itertools.permutations(n1,m)
for i in list(permute):
    print(' '.join(i))
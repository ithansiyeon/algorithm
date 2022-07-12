n,k = 5,3
a = [1,2,5,4,3]
b = [5,5,6,6,5]

a.sort()
b.sort(reverse=True)

a[:k], b[:k] = b[:k], a[:k]

print(sum(a))
import sys
sys.stdin = open("input", "rt")

n = int(input())
nums = input().split()

def reverse(x):
    return x[::-1]


def isPrime(x):
    Flag = [False] * (x + 1)
    Flag[0] = True
    Flag[1] = True

    for i in range(2,x+1):
        if not Flag[i]:
            for j in range(2,x+1):
                if i*j > x:
                    break
                else:
                    Flag[i*j] = True
    if not Flag[x]:
        return str(x)

result = []
for i in range(n):
    nums[i] = reverse(nums[i])
    result.append(isPrime(int(nums[i])))

print(" ".join(filter(lambda n:n!=None,result)))


import math
a,b = map(int,input().split(" "))
prime = [True]*(b+1)
# 에라토스테네스의 체란 간단히 설명하자면 일정 범위내 수열에서 배수들을 제거해 소수만 남기는 방법이다.
for i in range(2,int(math.sqrt(b))+1):
    if prime[i]:
        for j in range(2*i,b+1,i):
            prime[j] = False

for i in range(a,b+1):
    if i > 1 and prime[i]:
        print(i)

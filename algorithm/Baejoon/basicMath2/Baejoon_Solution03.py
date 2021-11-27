import math
import sys
n = int(sys.stdin.readline().rstrip())
# 루트를 씌운값이 중간값, 루트 n을 기준으로 같은 연산이 대칭이 된다.
# 이를 이용해 루트 n * 루트 n 이전의 소수로만 나눗셈을 수행한 후 나누어 떨어지지 않으면 소수
# i는 무조건 소수 어떤 수 n은 어떤 소수로 나누어지지 않을때까지 나누면 그 소수의 배수들로는 나누어지지 않는다.
for i in range(2,int(math.sqrt(n))+1):
    while n%i == 0:
        print(i)
        n//=i
if n > 1:
    print(n)

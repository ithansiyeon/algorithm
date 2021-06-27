# 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다. 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.
nums = int(input())
cnt = 0
for num in range(1,nums+1):
    num = str(num)
    if int(num) < 100:
        cnt+=1
    elif int(num) >= 100:
        n1 = int(num[0])
        n2 = int(num[1])
        n3 = int(num[2])
        if (n2 - n1) == (n3 - n2):
            cnt+=1
print(cnt)

def solution(price, money, count):
    answer = 0
    for i in range(count):
        answer+=(i+1)*price
    if answer-money > 0:
        return answer-money
    else: return 0
print(solution(3,20,1))
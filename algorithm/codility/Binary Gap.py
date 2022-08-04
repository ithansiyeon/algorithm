def solution(N):
    # write your code in Python 3.6
    cnt = 0
    result = 0
    print(bin(N))
    for i in bin(N)[2:]:
        if i == '1':
            result = max(result,cnt)
            cnt = 0
        else:
            cnt+=1
    return result

print(solution(6))
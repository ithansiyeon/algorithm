def solution(n, s):
    answer = []
    mok = s // n
    if mok == 0:
        return [-1]
    r = s % n
    while n >= 1:
        if r > 0:
            answer.append(mok+1)
            r-=1
        else:
            answer.append(mok)
        n -= 1
    return sorted(answer)

print(solution(2,9))
print(solution(2,1))
print(solution(2,8))
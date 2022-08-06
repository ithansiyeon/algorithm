def solution(S):
    s1 = "".join(sorted(S))
    if S != s1:
        return False
    else:
        return True

print(solution("abba"))
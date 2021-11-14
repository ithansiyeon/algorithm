def solution(s):
    answer = len(s)
    for i in range(1,len(s)//2+1):
        result = ""
        chars = s[:i]
        cnt = 1
        for j in range(i,len(s),i):
            if chars == s[j:j+i]:
                cnt+=1
            else:
                if cnt==1:
                    result+=chars
                else:
                    result+=str(cnt)+chars
                chars = s[j:j+i]
                cnt = 1
        if cnt == 1:
            result+=chars
        else:
            result+=str(cnt)+chars
        answer = min(len(result),answer)
    return answer

print(solution("xababcdcdababcdcd"))
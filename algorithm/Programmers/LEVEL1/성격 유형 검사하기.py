def solution(survey, choices):
    answer = ''
    personal = {'R':0,'T':0,'C':0,'F':0,'J':0,'M':0,'A':0,'N':0}
    for i in range(len(survey)):
        if choices[i] > 4:
            personal[survey[i][1]] += 1*abs(choices[i]-4)
        else:
            personal[survey[i][0]] += 1*abs(choices[i]-4)

    pstr = ['RT','CF','JM','AN']

    for i in range(4):
        if personal[pstr[i][0]] < personal[pstr[i][1]]:
            answer+=pstr[i][1]
        elif personal[pstr[i][0]] > personal[pstr[i][1]]:
            answer+=pstr[i][0]
        else:
            answer+=pstr[i][0]

    return answer

print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))

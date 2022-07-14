def solution(id_list, report, k):
    answer = {}
    result = {}
    answer1 = []
    report = list(set(report))
    for id in id_list:
        result[id] = 0
        answer[id] = 0

    for i in report:
        s = i.split(" ")
        result[s[1]]+=1

    for i in report:
        s = i.split(" ")
        if result[s[1]] >= k:
            answer[s[0]] +=1

    for i in id_list:
        answer1.append(answer[i])
    return answer1

print(solution(["con", "ryan"],["ryan con", "ryan con", "ryan con", "ryan con"],3))
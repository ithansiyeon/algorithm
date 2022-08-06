import copy

def solution(S):
    S = S.split("\n")
    result = []
    for l in S:
        result.append(l.split(", "))

    origin = copy.deepcopy(result)
    result.sort(key=lambda x : (x[1],x[2]))

    dic = {}
    cnt = 1

    for res in result:
        if res[1] not in dic.keys():
            cnt = 1
            dic[res[1]] = []
            dic[res[1]].append([str(cnt),res[1],res[0].split(".")[1],res[0],res[2]])
        else:
            cnt+=1
            dic[res[1]].append([str(cnt),res[1],res[0].split(".")[1],res[0],res[2]])

    for key,val in dic.items():
        for item in dic[key]:
            item[0]=item[0].zfill(len(str(len(dic[key]))))

    for o in origin:
        for key in dic.keys():
            if key == o[1]:
                for item in dic[key]:
                    if item[3] == o[0] and item[4] == o[2]:
                        o.append(item[0])
                break

    answer = []
    for o in origin:
        answer.append(o[1]+o[-1]+"."+o[0].split(".")[1])

    return "\n".join(answer)


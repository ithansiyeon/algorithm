# genres[i]: 고유번호가 i인 노래의 장르
# plays[i]: 고유번호가 i인 노래가 재생된 횟수
def solution(genres, plays):
    answer = []
    dic = {}
    for i in range(len(plays)):
        if genres[i] not in dic.keys():
            dic[genres[i]] = [[i,plays[i]]]
        else:
            dic[genres[i]].append([i,plays[i]])

    dic = dict(sorted(dic.items(), key=lambda x:sum([i[1] for i in x[1]]), reverse=True))

    for k in dic:
        b = sorted(dic[k],key=lambda x:(-x[1],x[0]))
        answer.append(b[0][0])
        if len(b) > 1:
            answer.append(b[1][0])

    return answer

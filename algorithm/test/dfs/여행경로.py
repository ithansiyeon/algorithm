def solution(tickets):
    dic = {}
    stack = []
    answer = []
    for i in tickets:
        if i[0] not in dic.keys():
            dic[i[0]] = [i[1]]
        else: dic[i[0]].append(i[1])
        dic[i[0]].sort(reverse=True)
    stack.append("ICN")
    while stack:
        tmp = stack[-1]
        if tmp not in dic.keys() or not dic[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(dic[tmp].pop())
    answer.reverse()
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))
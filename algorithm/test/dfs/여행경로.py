from collections import defaultdict


def solution(tickets):
    answer = []
    routes = defaultdict(list)
    for i in range(len(tickets)):
        routes[tickets[i][0]].append(tickets[i][1])

    for key in routes.keys():
        routes[key].sort(reverse=True)

    stack = ['ICN']
    while stack:
        tmp = stack[-1]
        if not routes[tmp]:
            answer.append(stack.pop())
        else:
            stack.append(routes[tmp].pop())
    answer.reverse()
    return answer

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))


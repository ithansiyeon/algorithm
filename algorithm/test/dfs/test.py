def dfs(graph, depth, chk, f):
    """
    재귀함수를 활용한 dfs
    :param graph: 전체 친구관계 리스트
    :param depth: 일직선으로 연결된 참가자의 수
    :param chk: 체크된 참가자
    :param f: 현재 기준이 되는 참가자
    :return: 문제의 요구조건 만족하면 1 리턴
    """
    chk.append(f)
    depth += 1
    if depth == 5:
        print(chk,depth)
        return 1

    for frnd in graph[f]:
        if frnd not in chk:
            r = dfs(graph, depth, chk, frnd)
            if r == 1:
                return 1

    chk.pop()
    depth -= 1

"""
1. 전체 친구의 관계를 리스트로 표현
    >> 참가자 N의 친구 리스트 = graph[N]
2. 0번 참가자부터 차례대로 첫번째 연결점으로 지정하고 일직선으로 연결되는 관계를 찾는다.

[예제]
5 5
0 1
1 2
2 3
3 0
1 4
"""
N, M = map(int, input().split())
graph = [[] for i in range(N)]
for m in range(M):
    r1, r2 = map(int, input().split())
    graph[r1].append(r2)
    graph[r2].append(r1)
print(graph)
result = 0
for i in range(N):
    _dfs = dfs(graph, 0, [], i)
    if _dfs == 1:
        result = _dfs
        break
print(result)






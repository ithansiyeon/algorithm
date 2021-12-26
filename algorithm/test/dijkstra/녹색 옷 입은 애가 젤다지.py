import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)  # 무한을 의미하는 10억
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 1


def dijkstra():
    q = []
    # 시작 노드로 가기 위한 비용은 (0,0) 위치의 값으로 설정하여, 큐에 삽입
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = graph[0][0]

    # 다익스트라 알고리즘 수행
    while q:
        # 가장 최단 거리가 짧은 노드에 대한 정보를 꺼냄
        cost, x, y = heapq.heappop(q)
        if x == n-1 and y == n-1:
            print(f'Problem {count}: {distance[x][y]}')
            break
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[x][y] < cost:
            continue
        # 현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 맵의 범위를 벗어나는 경우 무시
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]
                # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))

while True:
    # 노드의 개수를 입력
    n = int(input())
    if n == 0:
        break
    # 전체 맵 정보를 입력
    graph = [list(map(int, input().split())) for _ in range(n)]
    # 최단 거리 테이블을 모두 무한으로 초기화
    distance = [[INF] * n for _ in range(n)]
    dijkstra()
    count += 1
import heapq
def solution(n, works):
    heap = []
    for i in range(len(works)):
        heapq.heappush(heap,works[i]*(-1))
    while n > 0:
        if not heap:
            return 0

        maxx = -heapq.heappop(heap)
        maxx-=1

        if maxx > 0:
            heapq.heappush(heap, -maxx)
        n-=1
    return sum(work**2 for work in heap)

print(solution(3,[1,1]))
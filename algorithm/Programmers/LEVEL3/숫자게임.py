import heapq

def solution(a, b):
    a = [-i for i in a]
    b = [-i for i in b]
    heapq.heapify(a)
    heapq.heapify(b)
    answer = 0
    while b and a:
        am = heapq.heappop(a)
        bm = heapq.heappop(b)
        if -am < -bm:
            answer += 1
        else:
            heapq.heappush(b, bm)
    return answer

print(solution([5,1,3,7],[2,2,6,8]))
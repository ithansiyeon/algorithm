import sys
import heapq

n = int(sys.stdin.readline().rstrip())

heap = []
for i in range(n):
    heapq.heappush(heap,int(sys.stdin.readline().rstrip()))

result = 0
while len(heap) != 1:
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    sum_val = one + two
    result+=sum_val
    heapq.heappush(heap,sum_val)

print(result)


import sys
import heapq
sys.stdin = open("in5.txt", "rt")
heap = []
while True:
    a = int(input())
    if a == -1:
        break
    if a == 0:
        print(heapq.heappop(heap))
    else: heapq.heappush(heap,a)


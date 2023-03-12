import heapq
def solution(operations):
    heap = []
    for i in operations:
        a,b = i.split(" ")
        if a == "I":
            heap.append(int(b))
        elif a == "D":
            if b == "1":
                for i in range(len(heap)):
                    heap[i] = heap[i]*(-1)
                heapq.heapify(heap)
                if len(heap) != 0:
                    heapq.heappop(heap)
                for i in range(len(heap)):
                    heap[i] = heap[i]*(-1)
            else:
                if len(heap) != 0:
                    heapq.heapify(heap)
                    heapq.heappop(heap)
    if len(heap) == 0:
        heap = [0,0]
    else:
        heap = [max(heap),min(heap)]
    return heap

print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))
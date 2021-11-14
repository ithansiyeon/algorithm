from collections import deque

n = int(input())
queue = deque(list(range(1,n+1,1)))

while len(queue) != 1:
    queue.popleft()
    a = queue.popleft()
    queue.append(a)
print(queue[0])

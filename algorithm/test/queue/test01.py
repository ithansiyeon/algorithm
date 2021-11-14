import sys
from collections import deque

queue = deque()
def push(b):
    queue.append(b)

def pop():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue.popleft())

def size():
    print(len(queue))

def empty():
    if len(queue) == 0:
        print(1)
    else:
        print(0)

def front():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[0])

def back():
    if len(queue) == 0:
        print(-1)
    else:
        print(queue[-1])

n = int(input())
for i in range(n):
    a = sys.stdin.readline().rstrip()
    if "push" in a:
        b = a.split(" ")[1]
        push(int(b))
    elif a == "front":
        front()
    elif a == "back":
        back()
    elif a == "size":
        size()
    elif a == "empty":
        empty()
    elif a == "pop":
        pop()

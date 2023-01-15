from collections import deque
import sys

n = int(sys.stdin.readline().rstrip())
dlist = deque([])
def push_back(dlist,n):
    dlist.append(n)

def push_front(dlist,n):
    dlist.appendleft(n)

def pop_front(dlist):
    if len(dlist) == 0:
        print(-1)
    else:
        print(dlist.popleft())

def pop_back(dlist):
    if len(dlist) == 0:
        print(-1)
    else:
        print(dlist.pop())

def size(dlist):
    print(len(dlist))

def empty(dlist):
    if len(dlist) == 0:
        print(1)
    else:
        print(0)

def front(dlist):
    if len(dlist) == 0:
        print(-1)
    else:
        print(dlist[0])
def back(dlist):
    if len(dlist) == 0:
        print(-1)
    else:
        print(dlist[-1])

for i in range(n):
    alist = sys.stdin.readline().rstrip().split()
    if len(alist) == 1:
        if alist[0] == "front":
            front(dlist)
        elif alist[0] == "back":
            back(dlist)
        elif alist[0] == "size":
            size(dlist)
        elif alist[0] == "empty":
            empty(dlist)
        elif alist[0] == "pop_front":
            pop_front(dlist)
        elif alist[0] == "push_back":
            push_back(dlist)
        elif alist[0] == "push_front":
            push_front(dlist)
        elif alist[0] == "pop_back":
            pop_back(dlist)
    else:
        if alist[0] == "push_front":
            push_front(dlist, alist[1])
        elif alist[0] == "push_back":
            push_back(dlist, alist[1])


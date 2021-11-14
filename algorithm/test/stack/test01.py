import sys
n = int(sys.stdin.readline().rstrip())
stack = []
def push(a):
    stack.append(a)

def top():
    if len(stack) != 0:
        return stack[-1]
    else:
        return -1

def empty():
    if len(stack) == 0:
        return 1
    else:
        return 0

def size():
    return len(stack)

def pop():
    if len(stack) != 0:
        return stack.pop()
    else:
        return -1

for i in range(n):
    a = sys.stdin.readline().rstrip()
    slist = list(a.split(" "))
    if slist[0] == "push":
        push(slist[1])
    elif slist[0] == "top":
        print(top())
    elif slist[0] == "empty":
        print(empty())
    elif slist[0] == "size":
        print(size())
    elif slist[0] == "pop":
        print(pop())



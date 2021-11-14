n,k = map(int,input().split(" "))
queue = list(range(1,n+1))
answer = []
a = 0
while len(queue) != 0:
    a+=(k-1)
    a = a%len(queue)
    answer.append(str(queue.pop(a)))

print("<"+", ".join(answer)+">")

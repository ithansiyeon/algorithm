import math
from collections import deque

def solution(progresses, speeds):
    result = deque()
    for i in range(len(progresses)):
        result.append(math.ceil((100-progresses[i])/speeds[i]))
    cnt = 1
    answer = []
    print(result)
    max = result.popleft()
    while len(result) != 0:
       print(max,result[0])
       if max < result[0]:
           answer.append(cnt)
           cnt = 1
           max = result.popleft()
       else:
           cnt+=1
           result.popleft()
    answer.append(cnt)
    return answer

print(solution([93, 30, 55], [1, 30, 5]))
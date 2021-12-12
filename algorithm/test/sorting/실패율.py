def solution(N, stages):
    answer = []
    m = max(stages)
    if N > m:
        m = N
    data = [0]*(m+1)
    for i in range(len(stages)):
        data[stages[i]]+=1
    # print(data)
    for i in range(1,N+1):
        s = sum(data[i:])
        if s == 0:
            answer.append((i, 0))
        else: answer.append((i,data[i]/sum(data[i:])))
    # print(answer)
    answer = sorted(answer,key = lambda x : (-x[1],x[0]))
    answer = [x[0] for x in answer]
    return answer

print(solution(4,[1, 2, 3, 2, 1]))

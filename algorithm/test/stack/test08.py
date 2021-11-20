from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridges = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)
    sum = 0
    while bridges:
        answer+=1
        sum-=bridges.popleft()
        if truck_weights:
            if truck_weights[0]+sum <= weight:
                a = truck_weights.popleft()
                sum+=a
                bridges.append(a)
            else:
                bridges.append(0)
    return answer

print(solution(2,10,[7,4,5,6]))

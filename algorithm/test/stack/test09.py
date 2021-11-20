def solution(priorities, location):
    plist = [0]*len(priorities)
    plist[location] = 1
    cnt = 0
    while priorities:
        if priorities[0] == max(priorities):
            cnt += 1
            priorities.pop(0)
            if plist[0] == 1:
                break
            else:
                plist.pop(0)
        elif priorities[0] < max(priorities):
            plist.append(plist.pop(0))
            priorities.append(priorities.pop(0))

    return cnt

print(solution([1, 1, 1, 1, 1, 1],3))
def solution(n, times):
    start = 1
    times.sort()
    end = times[-1]*n
    result = 0
    while start <= end:
        mid = (start+end)//2
        p = 0
        for i in times:
            p+=mid//i
            if p > n:
                break
        if p >= n: # 사람을 더 볼 수 있으므로 시간을 줄이고
            end = mid-1
            result = mid
        else: # 시간이 부족해서 사람을 n보다 적게 보므로 시간을 늘린다
            start = mid+1
    return result
print(solution(6,[7, 10]))
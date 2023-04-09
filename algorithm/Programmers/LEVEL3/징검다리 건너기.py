def solution(stones, k):
    left, right = 1, max(stones)
    answer = 0 # 최대 인원수를 저장할 변수
    while left <= right:
        mid = (left + right) // 2
        cnt = 0
        check = True
        for stone in stones:
            if stone < mid:
                cnt += 1
                if cnt >= k: # mid 값 이하인 돌다리가 k개 이상이면 건널 수 없으므로 반복문 종료
                    check = False
                    break
            else:
                cnt = 0 # 연속된 돌다리 수 초기화
        if check:
            answer = mid # mid 값 이하인 돌다리가 k개 미만인 경우, 가능한 정답이므로 answer 값 업데이트 후 left 값을 늘려서 다시 탐색
            left = mid + 1
        else:
            right = mid - 1 # mid 값 이하인 돌다리가 k개 이상인 경우, 불가능한 정답이므로 right 값을 줄여서 다시 탐색
    return answer


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1],3))
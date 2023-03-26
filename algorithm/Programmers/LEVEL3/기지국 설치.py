def solution(n, stations, w):
    answer = 0
    start = 1
    idx = 0  # stations 리스트의 인덱스

    while start <= n:
        if idx < len(stations) and start >= stations[idx] - w:  # 기지국이 설치된 범위 안에 있는 경우
            start = stations[idx] + w + 1
            idx += 1
        else:  # 기지국이 설치되어 있지 않은 경우
            start += 2 * w + 1
            answer += 1

    return answer


print(solution(11,[4, 11],1))
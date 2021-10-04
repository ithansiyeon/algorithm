# 양의 정수 x에 대한 함수 f(x)를 다음과 같이 정의합니다.
#
# x보다 크고 x와 비트가 1~2개 다른 수들 중에서 제일 작은 수
# 예를 들어,
#
# f(2) = 3 입니다. 다음 표와 같이 2보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 3이기 때문입니다.
# 수	비트	다른 비트의 개수
# 2	000...0010
# 3	000...0011	1
# f(7) = 11 입니다. 다음 표와 같이 7보다 큰 수들 중에서 비트가 다른 지점이 2개 이하이면서 제일 작은 수가 11이기 때문입니다.
# 수	비트	다른 비트의 개수
# 7	000...0111
# 8	000...1000	4
# 9	000...1001	3
# 10	000...1010	3
# 11	000...1011	2
# 정수들이 담긴 배열 numbers가 매개변수로 주어집니다. numbers의 모든 수들에 대하여 각 수의 f 값을 배열에 차례대로 담아 return 하도록 solution 함수를 완성해주세요.
#
# 제한사항
# 1 ≤ numbers의 길이 ≤ 100,000
# 0 ≤ numbers의 모든 수 ≤ 1015
# 입출력 예
# numbers	result
# [2,7]	[3,11]

def solution(numbers):
    answer = []
    for div in numbers:
        if div < 2:
            answer.append(div + 1)
            continue
        binary = []
        print(binary)
        while div:
            div, mod = divmod(div, 2)
            binary.append(mod)

        for i in range(len(binary) - 1):
            if binary[i:i + 2] == [0, 0] or binary[i:i + 2] == [0, 1]:
                binary[i] = 1
                break

            if binary[i:i + 2] == [1, 0]:
                binary[i:i + 2] = [0, 1]
                break
        else:
            # 대신 for문 바깥쪽에 else문을 추가해서, break가 발생하지 않았을때의 동작에 대해 기술했다.
            binary[-1] = 0
            binary.append(1)

        base10 = 0
        for i in range(len(binary)):
            base10 += binary[i] * 2 ** i
            # **는 몇 승
        answer.append(base10)
    return answer

print(solution([9]))
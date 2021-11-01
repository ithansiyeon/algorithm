# n : 멀티탭 구멍의 개수, k : 전기 용품의 총 사용횟수
n,k = map(int,input().split(" "))
# 전기용품의 이름이 k이하의 자연수
plist = list(map(int,input().split(" ")))
# 멀티탭 n개의 구멍 역할을 할 리스트
array = []
# 개수를 세기 위한 변수
cnt = 0
for i in range(k):
   # 멀티탭에 전기 용품이 없을 경우
   if plist[i] not in array:
       # 아직 멀티탭에 꽃혀 있지 않음
       if len(array) < n:
            array.append(plist[i])
            continue
       # 멀티탭에 빈곳이 없는 경우
       else:
            cnt+=1
            index1 = -1
            index3 = -1
            # 단 한번도 쓰지 않을 기기를 빼거나 제일 마지막에 쓰일 기기를 뺌
            for j in range(n):
                try:
                    index2 = plist[i + 1:].index(array[j])
                    if index2 > index1:
                        index1 = index2
                        index3 = j
                except:
                    index3 = j
                    break
            # 사용 예정일 기기를 꽂음
            array[index3] = plist[i]
print(cnt)






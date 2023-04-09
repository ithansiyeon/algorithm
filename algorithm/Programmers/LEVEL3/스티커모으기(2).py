def solution(sticker):
    l = len(sticker)
    if l == 1:
        return sticker[0]
    
    dp1 = [0]*l
    dp1[0] = sticker[0]
    dp1[1] = dp1[0]
    
    for i in range(2,l):
        dp1[i] = max(dp1[i-2]+sticker[i],dp1[i-1])
    
    dp2 = [0]*l
    dp2[0] = 0
    dp2[1] = sticker[1]
    
    for i in range(2,l):
        dp2[i] = max(dp2[i-2]+sticker[i],dp2[i-1])

    return max(dp2[-1],dp1[-2])
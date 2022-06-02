from collections import deque
import sys
sys.stdin = open("in4.txt", "rt")
n = int(input())
nums = list(map(int,input().split()))
nums = deque(nums)
res = ""
num = [0]
while True:
    if len(nums) == 1 and num[-1] < nums[0]:
        res+="L"
        break
    l = nums[0]
    r = nums[-1]
    if l > r and num[-1] < r:
        res += "R"
        num.append(r)
        nums.pop()
    elif l <= r and num[-1] < l:
        res += "L"
        num.append(l)
        nums.popleft()
    elif num[-1] < r:
        res += "R"
        num.append(r)
        nums.pop()
    elif num[-1] < l:
        res += "L"
        num.append(l)
        nums.popleft()
    else:
        break

print(len(num)-1)
print(res)
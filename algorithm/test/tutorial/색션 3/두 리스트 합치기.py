import sys
sys.stdin = open("in5.txt", "rt")
n = int(input())
nums = []
nums2 = []
nums = list(map(int,input().split()))

n = int(input())
nums2 = list(map(int,input().split()))

print(' '.join(list(map(str,sorted(nums+nums2)))))
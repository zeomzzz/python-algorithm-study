# 풀이 1 : 정렬

N = int(input())

nums = list(map(int, input().split()))
nums.sort()

print(nums[0] * nums[N-1])


# 풀이 2 : min, max

N = int(input())

nums = list(map(int, input().split()))

print(min(nums) * max(nums))

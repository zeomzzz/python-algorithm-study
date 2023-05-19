import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = set(list(map(int, input().rstrip().split())))
nums = sorted(list(nums))

print(*nums)

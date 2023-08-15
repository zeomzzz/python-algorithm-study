import sys
input = sys.stdin.readline

N = int(input().rstrip())
nums = []
for _ in range(N) : nums.append(int(input().rstrip()))

nums.sort()

for i in nums : print(i)

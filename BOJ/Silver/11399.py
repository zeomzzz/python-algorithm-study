import sys
input = sys.stdin.readline

N = int(input().rstrip())
times = list(map(int, input().rstrip().split()))
times.sort()

dp = [0] * N
dp[0] = times[0]

for i in range(1, N) : dp[i] = dp[i - 1] + times[i]

print(sum(dp))

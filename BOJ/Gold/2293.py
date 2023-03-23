import sys
input = sys.stdin.readline

n, k = map(int, input().split()) # 동전 n개, 합계 가치 k
coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for c in coins : # 마지막에 올 동전 c
    for i in range(c, k + 1) :
        dp[i] += dp[i - c]

print(dp[-1])

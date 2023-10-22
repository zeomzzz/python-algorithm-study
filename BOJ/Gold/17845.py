import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
importances = [0] * (K + 1)
times = [0] * (K + 1)
for i in range(1, K + 1) :
    tmp_i, tmp_t = map(int, input().rstrip().split())
    importances[i], times[i] = tmp_i, tmp_t

dp = [[0] * (K + 1) for _ in range(N + 1)]
for i in range(1, K + 1) :
    for t in range(1, N + 1) :
        if times[i] <= t :
            dp[t][i] = max(importances[i] + dp[t - times[i]][i - 1], dp[t][i - 1])
        else :
            dp[t][i] = dp[t][i - 1]

print(dp[N][K])

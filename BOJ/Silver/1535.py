import sys
input = sys.stdin.readline

n = int(input())
loss = list(map(int, input().split()))
happ = list(map(int, input().split()))
loss.insert(0, 0)
happ.insert(0, 0)

dp = [[0] * 100 for _ in range(n + 1)] # 잃어버리는 체력의 범위 : 0 ~ 99

for i in range(1, n + 1) : # 사람 1 ~ n
    for j in range(0, 100) :

        dp[i][j] = dp[i-1][j]

        if loss[i] <= j :
            dp[i][j] = max(dp[i][j], dp[i-1][j-loss[i]] + happ[i])

print(dp[n][99])

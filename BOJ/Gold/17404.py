import sys
input = sys.stdin.readline

N = int(input().rstrip())
cost = [[0, 0, 0]] # 1번 인덱스에 1번 집. 집은 1 ~ N
for _ in range(N) :
    cost.append(list(map(int, input().rstrip().split())))

dp = [[0, 0, 0] for _ in range(N + 1)]

# 첫번째에 R을 칠한 경우
dp[1][0] = cost[1][0]
dp[1][1] = dp[1][2] = 1e9

for idx in range(2, N + 1) :
    dp[idx][0] = min(dp[idx-1][1], dp[idx-1][2]) + cost[idx][0]
    dp[idx][1] = min(dp[idx-1][0], dp[idx-1][2]) + cost[idx][1]
    dp[idx][2] = min(dp[idx-1][0], dp[idx-1][1]) + cost[idx][2]

ans = min(dp[N][1], dp[N][2]) # R로 끝나면 안되므로

# 첫번째에 G을 칠한 경우
dp[1][1] = cost[1][1]
dp[1][0] = dp[1][2] = 1e9

for idx in range(2, N + 1) :
    dp[idx][0] = min(dp[idx-1][1], dp[idx-1][2]) + cost[idx][0]
    dp[idx][1] = min(dp[idx-1][0], dp[idx-1][2]) + cost[idx][1]
    dp[idx][2] = min(dp[idx-1][0], dp[idx-1][1]) + cost[idx][2]

ans = min([ans, dp[N][0], dp[N][2]]) # G로 끝나면 안되므로

# 첫번째에 B을 칠한 경우
dp[1][2] = cost[1][2]
dp[1][0] = dp[1][1] = 1e9

for idx in range(2, N + 1) :
    dp[idx][0] = min(dp[idx-1][1], dp[idx-1][2]) + cost[idx][0]
    dp[idx][1] = min(dp[idx-1][0], dp[idx-1][2]) + cost[idx][1]
    dp[idx][2] = min(dp[idx-1][0], dp[idx-1][1]) + cost[idx][2]

ans = min([ans, dp[N][0], dp[N][1]]) # B로 끝나면 안되므로

print(ans)

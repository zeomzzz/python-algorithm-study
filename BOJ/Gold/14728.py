import sys
input = sys.stdin.readline

N, T = map(int, input().split()) # N : 시험 단원의 개수, T : 공부할 수 있는 시간
times = [0] # 예상 공부 시간
scores = [0] # 점수 -> 최대 점수 찾기

for _ in range(N) :
    K, S = map(int, input().split())
    times.append(K)
    scores.append(S)

dp = [[0] * (T + 1) for _ in range(N + 1)]

for i in range(1, N + 1) : # i번째 단원에 대해서
    for j in range(1, T + 1) :
        if times[i] <= j and dp[i-1][j] < dp[i-1][j-times[i]] + scores[i] :
            dp[i][j] = dp[i-1][j-times[i]] + scores[i]
        else :
            dp[i][j] = dp[i-1][j]

print(dp[N][T])

import sys
input = sys.stdin.readline

N = int(input().rstrip())
dp = [0 for _ in range(N + 1)]

works = [[] for _ in range(N + 1)]

for i in range(N) :
    t, p = map(int, input().rstrip().split()) # 기간 t, 금액 p
    if i + t < N + 1 : works[i + t].append([t, p]) # i + t일에 t일이 걸리는 p짜리 일이 끝남

for i in range(1, N + 1) :

    tmp = 0

    for t, p in works[i] : tmp = max(dp[i - t] + p, tmp)

    dp[i] = max(dp[i - 1], tmp)

print(dp[-1])

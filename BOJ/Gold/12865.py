import sys
input = sys.stdin.readline

N, K = map(int, input().split())  # n : 물품의 수, k : 버틸 수 있는 무게
ws = [0]  # 무게 담는 리스트 1 ~ N
vs = [0]  # 가치 담는 리스트 1 ~ N

for _ in range(N) :
    w, v = map(int, input().split())
    ws.append(w)
    vs.append(v)

dp = [[0] * (K + 1) for _ in range(N + 1)] # dp에는 최대 가치를 입력

for i in range(1, N + 1) : # 물건 1 ~ N에 대해서 확인 (담을 수 있다/없다)
    for k in range(1, K + 1) : # dp 1~K 까지 구함
        if ws[i] <= k : # 담을 수 있다 -> 담으면 max 맞나?
            dp[i][k] = max(dp[i-1][k], dp[i-1][k-ws[i]] + vs[i])
        else : # 담을 수 없다 -> 같은 무게 제한에서 안 담은 값으로..
            dp[i][k] = dp[i-1][k]

print(dp[N][K])

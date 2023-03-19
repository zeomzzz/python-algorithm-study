import sys
input = sys.stdin.readline

n = int(input())

lst = [[0, 0]]
for _ in range(n) :
    lst.append(list(map(int, input().split())))
    # [t, p] : t 기간, p 금액

dp = [0] * (n + 1)

# 1) i날에 상담을 하는 경우
# i-k날의 기간이 k+1일 때, dp[i - (k + 1)] + [i - k]의 가격 중 최대값이 dp[i]
# 2) i날에 상담을 하지 않는 경우 : i-1날 까지의 최대값이 i날까지의 최대값 -> dp[i] = dp[i-1]

for i in range(1, n + 1) :
    tmp = 0

    for j in range(i) :
        if lst[i - j][0] == j + 1 :
            tmp = dp[i - (j + 1)] + lst[i - j][1]
        else :
            tmp = dp[i - 1]

        if tmp > dp[i]: dp[i] = tmp

print(dp[-1])

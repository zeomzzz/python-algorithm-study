import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0] * (N + 1)
prev = [0] * (N + 1) # 이전에 몇 번에 들렀다 왔는지
dp[1] = 0
if N >= 2 :
    dp[2] = 1
    prev[2] = 1
if N >= 3 :
    dp[3] = 1
    prev[3] = 1

if N >= 4 :
    for i in range(4, N + 1) :
        if i % 6 == 0 :
            tmp = [dp[i - 1], dp[i // 3], dp[i // 2]]
            dp[i] = min(tmp) + 1

            if min(tmp) == dp[i - 1] : prev[i] = i - 1
            elif min(tmp) == dp[i // 3] : prev[i] = i // 3
            else : prev[i] = i // 2

        elif i % 3 == 0 :
            tmp = [dp[i - 1], dp[i // 3]]
            dp[i] = min(tmp) + 1

            if min(tmp) == dp[i - 1] : prev[i] = i - 1
            else : prev[i] = i // 3

        elif i % 2 == 0 :
            tmp = [dp[i - 1], dp[i // 2]]
            dp[i] = min(tmp) + 1

            if min(tmp) == dp[i - 1] : prev[i] = i - 1
            else : prev[i] = i // 2

        else :
            dp[i] = dp[i - 1] + 1
            prev[i] = i - 1

print(dp[N])

# 이전 찾기
idx = N
while True :

    if prev[idx] == 1 :
        print(str(idx) + " " + str(prev[idx]))
        break
    elif prev[idx] == 0 :
        print(idx, end = " ")
        break
    else :
        print(idx, end = " ")
        idx = prev[idx]

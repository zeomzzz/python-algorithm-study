import sys
input = sys.stdin.readline

N = int(input().rstrip())

if N % 2 == 1 : print(0)
else :
    dp = [0] * (N + 1)
    dp[0] = 1

    for i in range(2, N + 1, 2) :
        if i == 2 : dp[i] = 3
        else :
            dp[i] = dp[i - 2] * 3

            for j in range(4, N + 1, 2) : dp[i] += dp[i - j] * 2

    print(dp[-1])

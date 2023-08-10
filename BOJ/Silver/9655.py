import sys
input = sys.stdin.readline

N = int(input().rstrip())

dp = [0] * (N + 1)

if N > 0 : dp[1] = 1
if N > 1 : dp[2] = -1
if N > 2 : dp[3] = 1
if N > 3 :
    for i in range(4, N + 1) :
        if dp[i - 3] == 1 or dp[i - 1] == 1 : dp[i] = -1
        else : dp[i] = 1

if dp[N] ==  -1 : print("CY")
else : print("SK")

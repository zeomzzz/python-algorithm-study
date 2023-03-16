import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.insert(0, 0)

dp = [0] * (n + 1)
max_len = 0

for i in range(1, n + 1) :
    for j in range(i) :
        if A[i] > A[j] and dp[j] + 1 > dp[i] :
            dp[i] = dp[j] + 1
    if dp[i] > max_len : max_len = dp[i]

print(max_len)

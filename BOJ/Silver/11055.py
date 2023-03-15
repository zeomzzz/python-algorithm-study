import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A.insert(0, 0)

dp = [0] * (n + 1)
max = 0

for i in range(1, n + 1) :
    dp[i] = A[i]

    for j in range(0, i) :
        if A[j] < A[i] and dp[i] < dp[j] + A[i] :
            dp[i] = dp[j] + A[i]

    if dp[i] > max : max = dp[i]

print(max)

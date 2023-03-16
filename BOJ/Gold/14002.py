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

lst = []
idx = max_len

for i in range(n, 0, -1) :
    if idx == dp[i] :
        if len(lst) == 0 :
            lst.append(A[i])
            idx -= 1
        elif A[i] < lst[-1] :
            lst.append(A[i])
            idx -= 1

    if idx == 0 : break

lst.reverse()

print(*lst)

import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 수열 A의 크기 n
A = list(map(int, input().rstrip().split())) # 수열 A
A.insert(0, 1001) # 0번에 가장 큰 숫자보다 큰 1001 넣어줌

dp = [0] * (n + 1)

for i in range(1, n + 1) :
    for k in range(i) :
        if A[k] > A[i] and dp[k] + 1 > dp[i] :
            dp[i] = dp[k] + 1

print(max(dp))

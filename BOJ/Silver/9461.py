import sys
input = sys.stdin.readline

t = int(input()) # tc 개수

find_lst = [int(input()) for _ in range(t)]
n = max(find_lst) # n번쨰 삼각형까지 변의 길이 구해야 함

dp = [0] * (n + 1)

# k번째 삼각형 변의 길이 = k-1 번쨰 + k-5번째
for i in range(1, n + 1) :
    if i <= 3 : dp[i] = 1
    elif i == 4 : dp[i] = 2
    else : dp[i] = dp[i - 1] + dp[i - 5]

for f in find_lst :
    print(dp[f])

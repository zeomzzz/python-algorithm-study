import sys
input = sys.stdin.readline

N = int(input()) # 재료 N개
taste_S = [] # 신맛
taste_B = [] # 쓴맛

for _ in range(N) :
    s, b = map(int, input().split())
    taste_S.append(s)
    taste_B.append(b)

# 부분집합에 포함되면 신맛, 아니면 쓴맛
gap = 1e9
for i in range(1, 1 << N) :
    sum_S = 1 # 곱해야해서 1로 초기화
    sum_B = 0

    for j in range(N) :
        if (1 << j) & i :
            sum_S *= taste_S[j]
            sum_B += taste_B[j]

    if sum_S == 1 : sum_S = 0

    gap = min(gap, abs(sum_B - sum_S))

print(gap)

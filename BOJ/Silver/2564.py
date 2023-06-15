import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 가로 N, 세로 M
cnt = int(input().rstrip()) # 상점의 개수
total = (N + M) * 2

stores = [list(map(int, input().rstrip().split())) for _ in range(cnt)]
cur = list(map(int, input().rstrip().split()))

min_sum = 0

for dir, dist in stores :
    # 같은 사이드에 있음
    if cur[0] == dir :
        min_sum += abs(cur[1] - dist)
    # 반대 사이드에 있음 + 북남
    elif cur[0] + dir == 3 :
        min_sum += M + min(cur[1] + dist, N - cur[1] + N - dist)
    # 반대 사이드에 있음 + 동서
    elif cur[0] + dir == 7 :
        min_sum += N + min(cur[1] + dist, M - cur[1] + M - dist)
    # 옆에 있음
    elif cur[0] + dir == 4 :
        min_sum += cur[1] + dist
    elif cur[0] + dir == 6 :
        min_sum += N + M - (cur[1] + dist)
    elif cur[0] == 1 :
        min_sum += N - cur[1] + dist
    elif cur[0] == 4 :
        min_sum += cur[1] + N - dist
    elif cur[0] == 2 :
        min_sum += cur[1] + M - dist
    elif cur[0] == 3 :
        min_sum += M - cur[1] + dist

print(min_sum)

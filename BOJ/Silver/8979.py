import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split()) # 국가의 수 N, 등수를 알고 싶은 국가 K
scores = [list(map(int, input().rstrip().split())) for _ in range(N)]
scores.sort(key=lambda x : (-x[1], -x[2], -x[3]))

for i in range(N) :
    if scores[i][0] == K :
        idx = i

for i in range(N) :
    if scores[idx][1:] == scores[i][1:] :
        print(i + 1)
        break

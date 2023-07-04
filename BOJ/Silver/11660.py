import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 표의 크기 N, 합을 구해야 하는 횟수 M

graph = [[0 for i in range(N + 1)]]
for _ in range(N) :
    tmp = [0] + list(map(int, input().rstrip().split()))
    graph.append(tmp)

# 부분합 구하기
for r in range(1, N + 1) :
    for c in range(1, N + 1) :
        graph[r][c] += graph[r-1][c] + graph[r][c-1] - graph[r-1][c-1]

for _ in range(M) :
    x1, y1, x2, y2 = map(int, input().rstrip().split())

    print(graph[x2][y2] - graph[x2][y1-1] - graph[x1-1][y2] + graph[x1-1][y1-1])

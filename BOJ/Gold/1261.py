import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

M, N = map(int, input().rstrip().split()) # 가로 M, 세로 N
maze = [list(input().rstrip()) for _ in range(N)]
dist = [[INF] * M for _ in range(N)]
visited = [[0] * M for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

heap = []
heapq.heappush(heap, (0, 0, 0)) # w, r, c
dist[0][0] = 0
visited[0][0] = 1

while heap :

    cw, cr, cc = heapq.heappop(heap)

    for i in range(4) :
        nr = cr + dr[i]
        nc = cc + dc[i]

        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc]:
            nw = cw
            if maze[nr][nc] == '1' :
                nw = cw + 1

            if dist[nr][nc] >= nw :
                dist[nr][nc] = nw
                visited[nr][nc] = 1
                heapq.heappush(heap, (nw, nr, nc))

print(dist[N - 1][M - 1])

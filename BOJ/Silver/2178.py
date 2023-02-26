from collections import deque
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
maze = [list(map(int, sys.stdin.readline().rstrip()[:])) for _ in range(n)]
visited = [[0] * m for _ in range(n)]

dr = [0, 0, 1, -1] # 상, 하, 좌, 우
dc = [1, -1, 0, 0]

def bfs(a, b) :
    q = deque()
    q.append([a, b])

    visited[a][b] += 1 # (a, b) 방문해서 +1

    while q :
        a, b = q.popleft()

        for i in range(4) : # 사방 탐색
            nr = a + dr[i]
            nc = b + dc[i]

            # 새로운 위치가 범위 내이면서 이동 가능한 곳이고 방문하지 않았을 때(최소 거리이므로)
            if 0 <= nr < n and 0 <= nc < m and maze[nr][nc] == 1 and not visited[nr][nc]:
                q.append([nr, nc])
                visited[nr][nc] += visited[a][b] + 1

    return visited[n - 1][m - 1]

print(bfs(0, 0))

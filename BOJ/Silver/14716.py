import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int, input().rstrip().split()) # 세로 M, 가로 N
banners = [list(map(int, input().rstrip().split())) for _ in range(M)]

dr = [-1, 1, 0, 0, -1, -1, 1, 1]
dc = [0, 0, -1, 1, 1, -1, 1, -1]

q = deque()
cnt = 0

for r in range(M) :
    for c in range(N) :
        if banners[r][c] :
            cnt += 1
            q.append((r, c))
            banners[r][c] = 0

            while q :
                cr, cc = q.popleft()

                for i in range(8) :
                    nr, nc = cr + dr[i], cc + dc[i]
                    if 0 <= nr < M and 0 <= nc < N and banners[nr][nc] :
                        q.append((nr, nc))
                        banners[nr][nc] = 0
print(cnt)

from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # 세로 n, 가로 m
land = [list(map(int, input().rstrip().split())) for _ in range(n)]

tr, tc = 0, 0
for r in range(n) :
    for c in range(m) :
        if land[r][c] == 2 : tr, tc = r, c
        elif land[r][c] == 1 : land[r][c] = -1

q = deque()
q.append((tr, tc))
land[tr][tc] = 0 # 타겟까지는 거리 0

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

while q :
    cr, cc = q.popleft()

    for i in range(4) :
        nr, nc = cr + dr[i], cc + dc[i]

        if 0 <= nr < n and 0 <= nc < m and land[nr][nc] != 0 :
            if land[nr][nc] == -1 or (land[nr][nc] != 0 and land[nr][nc] > land[cr][cc] + 1) :
                land[nr][nc] = land[cr][cc] + 1
                q.append((nr, nc))

for l in land : print(*l)

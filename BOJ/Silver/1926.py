import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())  # 세로 n, 가로 m
pictures = [list(map(int, input().rstrip().split())) for _ in range(n)]

q = deque()

def bfs(r, c) :
    global q

    size = 1

    q.append((r, c))
    pictures[r][c] = 0

    while q :
        cr, cc = q.popleft()
        pictures[cr][cc] = 0

        dr = [-1, 1, 0, 0]
        dc = [0, 0, -1, 1]

        for i in range(4) :
            nr, nc = cr + dr[i], cc +dc[i]

            if 0 <= nr < n and 0 <= nc < m and pictures[nr][nc] == 1 :
                pictures[nr][nc] = 0
                q.append((nr, nc))
                size += 1

    return size

cnt = 0
max_size = 0

for r in range(n) :
    for c in range(m) :
        if pictures[r][c] == 1 :
            cnt += 1
            max_size = max(max_size, bfs(r, c))

print(cnt)
print(max_size)

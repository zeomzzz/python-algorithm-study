from collections import deque
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def bfs() :
    global tmp_lab, safe_max

    tmp_lab = []
    for r in range(n) :
        line = lab[r][:]
        tmp_lab.append(line)

    q = deque()

    for r in range(n) :
        for c in range(m) :
            if tmp_lab[r][c] == 2 :
                q.append([r, c])

    while q :
        x, y = q.popleft()

        dr = [1, -1, 0, 0]
        dc = [0, 0, 1, -1]

        for i in range(4) :
            nr = x + dr[i]
            nc = y + dc[i]
            if 0 <= nr < n and 0 <= nc < m and tmp_lab[nr][nc] == 0 :
                tmp_lab[nr][nc] = 2
                q.append([nr, nc])

    safe = 0
    for r in range(n):
        for c in range(m):
            if tmp_lab[r][c] == 0:
                safe += 1
    safe_max = max(safe_max, safe)


def comb(depth, idx) :

    # base
    if depth == 3 :
        bfs()
        return
    if idx == len(walls) :
        return

    # recursive
    lab[walls[idx][0]][walls[idx][1]] = 1
    comb(depth+1, idx+1)
    lab[walls[idx][0]][walls[idx][1]] = 0
    comb(depth, idx+1)


n, m = map(int, input().split()) # 세로 n, 가로 m
lab = [list(map(int, input().split())) for _ in range(n)]
safe_max = 0 # 안전영역의 최대값

walls = []
for r in range(n) :
    for c in range(m) :
        if lab[r][c] == 0 :
            walls.append([r, c])

comb(0, 0)

print(safe_max)

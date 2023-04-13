import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

N = int(input())
graph = [list(input().rstrip()) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
visited1 = [[0] * (N) for _ in range(N)]
visited2 = [[0] * (N) for _ in range(N)]

def dfs1(r, c, color) : # not 적록색약
    visited1[r][c] = 1

    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N and not visited1[nr][nc] and graph[nr][nc] == color :
            dfs1(nr, nc, color)

def dfs2(r, c, color):  # 적록색약
    visited2[r][c] = 1

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]

        if color == 'B' :
            if 0 <= nr < N and 0 <= nc < N and not visited2[nr][nc] and graph[nr][nc] == color:
                dfs2(nr, nc, color)
        else :
            if 0 <= nr < N and 0 <= nc < N and not visited2[nr][nc] and graph[nr][nc] != 'B':
                dfs2(nr, nc, color)

cnt1 = 0
cnt2 = 0
for r in range(N) :
    for c in range(N) :
        # not 적록색약
        if not visited1[r][c] :
            cnt1 += 1
            dfs1(r, c, graph[r][c])

        # 적록색약
        if not visited2[r][c] :
            cnt2 += 1
            dfs2(r, c, graph[r][c])

print(str(cnt1) + ' ' + str(cnt2))

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

def dfs(cr, cc) :
    global maps

    dr = [-1, -1, -1, 1, 1, 1, 0, 0, 0]
    dc = [-1, 0, 1, -1, 0, 1, -1, 0, 1]

    for i in range(9) :
        nr, nc = cr + dr[i], cc + dc[i]

        if 0 <= nr < h and 0 <= nc < w and maps[nr][nc] == 1 :
            maps[nr][nc] = -1
            dfs(nr, nc)


while True :
    w, h = map(int, input().rstrip().split()) # 지도의 너비 w, 높이 h
    if w == 0 and h == 0 : break

    maps = [list(map(int, input().rstrip().split())) for _ in range(h)]

    cnt = 0

    for r in range(h) :
        for c in range(w) :

            if maps[r][c] == 1 :
                cnt += 1
                maps[r][c] = -1
                dfs(r, c)

    print(cnt)

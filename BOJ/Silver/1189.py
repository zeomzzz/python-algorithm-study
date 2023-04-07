import sys
input = sys.stdin.readline

# 왼쪽 아래에서 출발, 오른쪽 위에 도착
def backtracking(cr, cc, depth) :
    global ans

    # base
    if depth == k :
        if cr == 0 and cc == c-1 :
            ans += 1
        return

    else :
        for i in range(4) :
            nr = cr + dr[i]
            nc = cc + dc[i]

            if 0 <= nr < r and 0 <= nc < c and graph[nr][nc] == "." :
                graph[nr][nc] = graph[cr][cc] + 1
                backtracking(nr, nc, depth + 1)
                graph[nr][nc] = "."


r, c, k = map(int, input().split()) # r : 세로, c : 가로, k : 거리
graph = [list(input().rstrip()) for _ in range(r)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

ans = 0
graph[r-1][0] = 1
backtracking(r-1, 0, 1)

print(ans)

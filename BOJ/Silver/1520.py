import sys
sys.setrecursionlimit(10 ** 6)

m, n = map(int, sys.stdin.readline().rstrip().split())

graph = []
for _ in range(m) :
    graph.append(list(map(int, sys.stdin.readline().rstrip().split())))

visited = [[-1 for _ in range(n)] for _ in range(m)]

dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

def dfs(r, c) :
    # visited == -1 이어서 탐색했을 때 목적지에 도착하면 +1
    if r == m - 1 and c == n - 1 :
        return 1

    if visited[r][c] == -1 :
        visited[r][c] = 0

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < m and 0 <= nc < n and graph[r][c] > graph[nr][nc] :
                visited[r][c] += dfs(nr, nc)

    return visited[r][c]

print(dfs(0, 0))

import sys
sys.setrecursionlimit(10 ** 6)

n, m, k = map(int, sys.stdin.readline().rstrip().split()) # n : 세로, m : 가로, k : 음식물 쓰레기 개수
graph = [[0] * (m + 1) for _ in range(n + 1)]
visited = [[0] * (m + 1) for _ in range(n + 1)]

for _ in range(k) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1

def dfs(r, c) :

    global size
    visited[r][c] = 1
    graph[r][c] = 0

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    for i in range(4) :
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 < nr < n + 1 and 0 < nc < m + 1 and graph[nr][nc] and not visited[nr][nc]:
            size += 1
            graph[nr][nc] = 0
            dfs(nr, nc)

    return size

maxSize= 0
for r in range(1, n + 1) :
    for c in range(1, m + 1) :
       if graph[r][c] and not visited[r][c] :
           size = 1 # 음식물 처음 사이즈는 1
           tmp = dfs(r, c)
           maxSize = max(maxSize, tmp)

print(maxSize)

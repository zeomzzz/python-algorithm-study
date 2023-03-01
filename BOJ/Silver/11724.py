import sys
sys.setrecursionlimit(10 ** 6)

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(m) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

ans = 0

def dfs(v) :

    visited[v] = 1

    for i in range(1, n + 1) :
        if not visited[i] and graph[i][v] :
            dfs(i)


for i in range(1, n + 1) :
    if not visited[i] :
        dfs(i)
        ans += 1

print(ans)

import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # 사람의 수 n, 친구 관계의 수 m
graph = [[] for _ in range(n)]
for _ in range(m) :
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

ans = 0

# 출발점에서 출발해서 dfs 로 depth 4까지 갈 수 있는지
def dfs(cur, depth) :
    global ans, visited

    visited[cur] = 1 # 방문처리

    if depth == 4 :
        ans = 1
        return

    for nxt in graph[cur] :
        if ans : break

        if not visited[nxt] :
            dfs(nxt, depth + 1)
            visited[nxt] = 0 # 복구

for cur in range(n) :
    visited = [0] * n
    dfs(cur, 0)

    if ans : break

print(ans)

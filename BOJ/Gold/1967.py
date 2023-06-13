import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n = int(input().rstrip()) # 노드의 개수 n
graph = [[] for _ in range(n + 1)]

for _ in range(n - 1) :
    parent, child, w = map(int, input().rstrip().split())
    graph[parent].append((child, w))
    graph[child].append((parent, w))

def dfs(cur, distance) :
    for nxt, w in graph[cur] :
        if visited[nxt] == -1 :
            visited[nxt] = distance + w
            dfs(nxt, distance + w)

visited = [-1] * (n + 1)
visited[1] = 0
dfs(1, 0)

end = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[end] = 0
dfs(end, 0)

print(max(visited))

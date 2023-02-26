import sys

t = int(sys.stdin.readline().rstrip())

def dfs(v) :

    visited[v] = True
    country.append(v) # 방문한 국가 추가

    for i in range(1, n + 1) :
        if not visited[i] and graph[v][i] : # 아직 방문 안했고 연결되어 있을 때
            dfs(i)


for _ in range(t) :

    n, m = map(int, sys.stdin.readline().rstrip().split()) # 국가의 수 n, 비행기 종류 m
    graph = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [False] * (n + 1)
    country = [] # 방문한 국가를 담음

    for i in range(m) :
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a][b] = 1
        graph[b][a] = 1

    dfs(1)
    print(len(country) - 1)

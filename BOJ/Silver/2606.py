import sys

n = int(sys.stdin.readline().rstrip()) # 컴퓨터 수 n
com = [[0] * (n + 1) for _ in range(n + 1)] # 컴퓨터 연결관계 담은 리스트
m = int(sys.stdin.readline().rstrip()) # 연결관계 쌍의 수 m
visited = [0] * (n + 1)

# 컴퓨터 연결관계 입력
for i in range(m) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    com[a][b] = 1
    com[b][a] = 1

def dfs(v) :
    visited[v] = True

    for i in range(n+1) :
        if not visited[i] and com[v][i] : # i를 아직 방문하지 않았고 v와 연결되어 있을 때
            dfs(i)

dfs(1)
print(visited.count(1) - 1) # 1번 뺌

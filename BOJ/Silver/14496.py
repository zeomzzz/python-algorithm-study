import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
N, M = map(int, input().rstrip().split()) # N개의 문자, 치환 가능한 문자쌍 M개
graph = [[] for _ in range(N + 1)]

for i in range(M) :
    j, k = map(int, input().rstrip().split())
    graph[j].append(k)
    graph[k].append(j)

visited = [0 for _ in range(N + 1)]
visited[a] = 1

q = deque()
q.append((a, 0))

ans = -1
while q :
    cur, dist = q.popleft()

    if cur == b :
        ans = dist
        break

    for nxt in graph[cur] :
        if not visited[nxt] :
            visited[nxt] = 1
            q.append((nxt, dist + 1))

print(ans)

import sys, heapq
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 건물의 개수 N, 도로의 개수 M
edges = [[] for _ in range(N + 1)]
heap = []
max_cost = 0
visited = [0] * (N + 1)
res = 0

for _ in range(M) :
    a, b, c = map(int, input().rstrip().split()) # 건물번호 a, b, 비용 c
    edges[a].append((c, b))
    edges[b].append((c, a))
    max_cost += c

for edge in edges[1] :
    heapq.heappush(heap, edge)

visited[1] = 1

while heap :
    w, cur = heapq.heappop(heap)

    if not visited[cur] :
        visited[cur] = 1
        res += w

        for next in edges[cur] :
            if not visited[next[1]] :
                heapq.heappush(heap, next)

if sum(visited) != N :
    print(-1)
else :
    print(max_cost - res)

import sys, heapq
input = sys.stdin.readline

v, e = map(int, input().split()) # 정점 v개 (1~v), 간선 e개
k = int(input()) # 시작 정점 k
graph = [[] for _ in range(v + 1)]

for _ in range(e) :
    u, x, w = map(int, input().split())
    graph[u].append([x, w])

distance = [sys.maxsize] * (v + 1)

# 다익스트라
q = []
heapq.heappush(q, (0, k)) # 첫번째 노드까지 거리는 0

distance[k] = 0

while q :
    dist, cur = heapq.heappop(q)

    if distance[cur] < dist :
        continue

    for nxt in graph[cur] :
        cost = dist + nxt[1]
        if cost < distance[nxt[0]]:
            distance[nxt[0]] = cost
            heapq.heappush(q, (cost, nxt[0]))

for i in range(1, v + 1) :
    if distance[i] == sys.maxsize :
        print("INF")
    else :
        print(distance[i])

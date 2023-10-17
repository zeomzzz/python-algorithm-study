import sys
input = sys.stdin.readline
import heapq

n, m, r = map(int, input().rstrip().split()) # n : 지역 개수, m : 수색 범위, r : 길의 개수
items = list(map(int, input().rstrip().split()))
items.insert(0, 0)
edge = [[] for _ in range(n + 1)]
for _ in range(r) :
    v1, v2, w = map(int, input().rstrip().split())
    edge[v1].append([v2, w])
    edge[v2].append([v1, w])

max_items = 0 # item 최대 개수 기록
INF = sys.maxsize

for region in range(1, n + 1) :
    dist = [INF] * (n + 1)
    dist[region] = 0
    heap = []
    heapq.heappush(heap, (0, region))

    while heap :
        w, v = heapq.heappop(heap)

        if w != dist[v] : continue

        for nv, nw in edge[v] :
            if dist[nv] > dist[v] + nw :
                dist[nv] = dist[v] + nw
                heapq.heappush(heap, (dist[nv], nv))

    tmp = 0
    for i in range(1, n + 1) :
        if dist[i] <= m : tmp += items[i]

    if tmp > max_items : max_items = tmp

print(max_items)

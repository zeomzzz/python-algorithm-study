import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip()) # N : 도시의 개수
M = int(input().rstrip()) # M : 버스의 개수
INF = sys.maxsize
dist = [INF] * (N + 1)

edges = [[] for _ in range(N + 1)]
for _ in range(M) :
    st, ed, w = map(int, input().rstrip().split())
    edges[st].append((w, ed))

A, B = map(int, input().rstrip().split())  # A, B : 출발, 도착

heap = []
heapq.heappush(heap, (0, A))
dist[A] = 0

while heap :
    cw, cv = heapq.heappop(heap)

    if cw != dist[cv] : continue

    for nw, nv in edges[cv] :
        if dist[nv] > dist[cv] + nw :
            dist[nv] = dist[cv] + nw
            heapq.heappush(heap, (dist[nv], nv))

print(dist[B])

import sys, heapq
input = sys.stdin.readline
INF = sys.maxsize

N, E = map(int, input().rstrip().split())  # N : 정점의 개수, E : 간선의 개수

edges = [[] for _ in range(N + 1)]
for _ in range(E) :
    a, b, c = map(int, input().rstrip().split()) # a에서 b까지 거리가 c
    edges[a].append((c, b))
    edges[b].append((c, a))

v1, v2 = map(int, input().rstrip().split()) # 반드시 거쳐야 하는 정점 v1, v2

'''
1) 1 -> v1 -> v2 -> N
2) 1 -> v2 -> v1 -> N
'''

# 1. 출발점 heap에 넣고 거리는 0
def d(start) :
    dist = [INF] * (N + 1)

    heap = []

    heapq.heappush(heap, (0, start))
    dist[start] = 0

    # heap이 빌 때까지 반복문 돌리기
    while heap :
        cw, cv = heapq.heappop(heap)

        if cw != dist[cv] : continue
        for nw, nv in edges[cv] :
            if dist[nv] > dist[cv] + nw :
                dist[nv] = dist[cv] + nw
                heapq.heappush(heap, (dist[nv], nv))

    return dist

d1 = d(1)
dv1 = d(v1)
dv2 = d(v2)

ans1 = d1[v1] + dv1[v2] + dv2[N]
ans2 = d1[v2] + dv2[v1] + dv1[N]

if ans1 >= INF and ans2 >= INF :
    print(-1)
else :
    print(min(ans1, ans2))

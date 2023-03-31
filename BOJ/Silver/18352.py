import sys, heapq
input = sys.stdin.readline

def djk(start) :
    global dist, cities

    heap = []
    heapq.heappush(heap, (0, start))
    dist[start] = 0

    while heap :
        curd, cur = heapq.heappop(heap)
        if dist[cur] < curd : continue # 지금이 더 작으면 갱신 안함 (== 이미 방문 한 것)

        for i in cities[cur] :
            cost = curd + i[1]
            if dist[i[0]] > cost :
                dist[i[0]] = cost
                heapq.heappush(heap, (cost, i[0]))

n, m, k, x = map(int, input().split()) # 도시 n개(1 ~ n), 도로 m개, 거리 k, 출발도시 x

cities = [[] for _ in range(n + 1)]
for _ in range(m) :
    r, c = map(int, input().split())
    cities[r].append((c, 1))

dist = [300001] * (n + 1)

djk(x)

ans = []
for i in range(1, n + 1) :
    if dist[i] == k :
        ans.append(i)

if len(ans) == 0 :
    print(-1)
else :
    for i in ans : print(i)

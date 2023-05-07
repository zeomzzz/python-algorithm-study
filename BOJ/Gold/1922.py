import sys, heapq
input = sys.stdin.readline

N = int(input().rstrip()) # 컴퓨터의 수 N
M = int(input().rstrip()) # 연결할 수 있는 선의 수 M
heap = []
visited = [0] * (N + 1) # 각 노드 방문 여부 확인
ans = 0

# 인접 리스트에 간선 정보 넣기
edges = [[] for _ in range(N + 1)]

for _ in range(M) :
    a, b, c = map(int, input().rstrip().split()) # c : 가중치
    edges[a].append([c, b])
    edges[b].append([c, a])

# 첫번째 노드 넣기
for edge in edges[1] :
    heapq.heappush(heap, edge)

visited[1] = 1 # 출발 노드 방문처리

# heap 빌 때 까지..
while heap :
    w, cur = heapq.heappop(heap)

    if not visited[cur] : # 아직 방문 안했으면
        visited[cur] = 1 # visited로 바꾸고
        ans += w # 가중치 더해줌

        for next in edges[cur] : # 연결된 노드 중
            if not visited[next[1]] : # 아직 방문 안한 노드면
                heapq.heappush(heap, next) # heap에 넣기

print(ans)

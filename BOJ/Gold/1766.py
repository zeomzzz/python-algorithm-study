# 위상정렬 + 우선순위큐

import sys, heapq
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())  # n : 문제의 수 , m : 정보 개수

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
hq = []
ans = []

for _ in range(m) :
    a, b = map(int, input().rstrip().split())
    graph[a].append(b) #  a -> b
    indegree[b] += 1 # 선행조건 추가

for i in range(1, n + 1) :
    if indegree[i] == 0 : heapq.heappush(hq, i)  # 선행조건 없으면 q에 넣기

while hq :

    cur = heapq.heappop(hq)
    ans.append(cur)

    for nxt in graph[cur] :
        indegree[nxt] -= 1 # 선행조건 하나 완료
        if indegree[nxt] == 0 :
            heapq.heappush(hq, nxt) # 선행조건 다 완료되면 큐에 넣기

print(*ans)

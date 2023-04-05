from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())  # n : 가수의 수, m : 보조 PD의 수

graph = [[] * (n + 1) for _ in range(n + 1)]
indegree = [0] * (n + 1)
q = deque()
ans = []

for _ in range(m) :
    tmp = list(map(int, input().split()))
    x = tmp[0]  # 담당한 가수의 수

    if x <= 1 : continue

    # 선행 관계 넣어주기
    # 보조 출연자 순서 : tmp[1] 부터(포함) x개 -> x-1개까지 쌍
    for i in range(1, x) :
        if tmp[i + 1] not in graph[tmp[i]] :
            graph[tmp[i]].append(tmp[i + 1])
            indegree[tmp[i + 1]] += 1

# 선행 조건 없는거 q에 넣어주기
for i in range(1, n + 1) :
    if indegree[i] == 0 : q.append(i)

# q 빌 때까지 반복문 ㄱ
isCycle = False
while q and not isCycle :
    cur = q.popleft()
    ans.append(cur)

    for nxt in graph[cur] :

        if cur in graph[nxt] : # 사이클 있으면 종료
            isCycle = True
            break

        indegree[nxt] -= 1 # 선행조건 하나 해결

        if indegree[nxt] == 0 : q.append(nxt)

if len(ans) == n :
    for a in ans : print(a)
else : print(0)

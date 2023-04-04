from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # n : 학생 수(1 ~ n), m : 비교 횟수

graph = [[0] for _ in range(n + 1)]
indegree = [0] * (n + 1) # 선행 조건 개수
ans = []

for _ in range(m) :
    a, b = map(int, input().rstrip().split()) # a가 b보다 앞에 서야 한다
    graph[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, n + 1) :
    if indegree[i] == 0 : q.append(i)

while q :

    cur = q.popleft() # 하나 꺼냄 (방문 완)
    ans.append(cur)

    for next in graph[cur] :
        indegree[next] -= 1 # 선행조건 하나 감소

        if indegree[next] == 0 :
            q.append(next) # 선행조건 다 끝나면 넣기

print(*ans)

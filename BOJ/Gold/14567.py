from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # n : 과목의 수, m : 선수 조건의 수

graph = [[0] for _ in range(n + 1)]
indegree = [0] * (n + 1)
sms = [0] * (n + 1)  # 이수 학기

for _ in range(m) :
    a, b = map(int, input().rstrip().split()) # a가 b의 선수과목
    graph[a].append(b)
    indegree[b] += 1

q = deque()

for i in range(1, n + 1) :
    if indegree[i] == 0 :
        q.append(i) # 선행 조건 없는 애들 먼저 담기
        sms[i] = 1 # 1학기에 들어야지

while q :

    cur = q.popleft()

    for nxt in graph[cur] :
        indegree[nxt] -= 1 # 선행과목 하나 이수 완

        if indegree[nxt] == 0 : # 다음 과목의 선행과목 다 들었으면
            sms[nxt] = sms[cur] + 1 # 지금 과목 다음학기에 들어야지
            q.append(nxt)

print(*sms[1:])

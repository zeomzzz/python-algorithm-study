import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
visited = [0] * 200001  # 경로의 길이 기록

if N == K :
    cnt = 1
else :

    q = deque()
    q.append(N) # 출발점 넣기
    cnt = 0

    while q :

        cur = q.popleft()

        dr = [-1, +1, +cur]

        for i in range(3) :
            nxt = cur + dr[i]
            if 0 <= nxt < 200001 :

                # 첫 방문 또는 이미 방문했는데 최단경로인 경우
                if not visited[nxt] or visited[nxt] == visited[cur] + 1 :
                    q.append(nxt)
                    visited[nxt] = visited[cur] + 1

                    if nxt == K : # K에 도달했고 최단경로인 경우
                        cnt += 1

print(visited[K])
print(cnt)

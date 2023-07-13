import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().rstrip().split()) # 수빈이 위치 N, 동생 위치 K

visited = [-1] * 200001

ans = sys.maxsize

q = deque()
q.append(N)
visited[N] += 1

while q :
    cur = q.popleft()

    dx = [-1, 1, cur]

    for i in range(3) :
        nxt = cur + dx[i]

        if 0 <= nxt < 200001 :
            if i == 2 and (visited[nxt] == -1 or visited[cur] < visited[nxt]) :
                visited[nxt] = visited[cur]
                q.append(nxt)
            elif (i == 0 or i == 1) and (visited[nxt] == -1 or visited[cur] + 1 < visited[nxt]) :
                visited[nxt] = visited[cur] + 1
                q.append(nxt)

            if nxt == K : ans = min(ans, visited[nxt])

print(ans)

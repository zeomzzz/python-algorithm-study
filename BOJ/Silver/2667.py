import sys
from collections import deque

n = int(sys.stdin.readline().rstrip()) # 지도의 크기
house = [list(map(int, sys.stdin.readline().rstrip()[:])) for _ in range(n)] # 집 정보 입력
ans = []

def bfs(r, c) :
    q = deque()
    q.append([r, c])
    house[r][c] = 0 #큐에 추가하고 방문 처리
    cnt = 1

    # 인접한 곳에 집이 있어야 하므로 사방탐색
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    while q :
        r, c = q.popleft()

        for i in range(4) :
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < n and 0 <= nc < n and house[nr][nc] == 1 : # 인접한 곳에 집이 있으면
                q.append([nr, nc])
                house[nr][nc] = 0
                cnt += 1

    return cnt

for i in range(n) :
    for j in range(n) :
        if house[i][j] == 1 : # 집이 있을 때 탐색 시작
            ans.append(bfs(i, j))

ans.sort()

print(len(ans))
for i in ans :
    print(i)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c) : # 분리되었는지 확인하기 위한 bfs
    q = deque()
    q.append((r, c))
    visited[r][c] = 1

    while q :
        cr, cc = q.popleft()

        for i in range(4) :
            nr, nc = cr + dr[i], cc + dc[i]

            if 0 <= nr < N and 0 <= nc < M and iceberg[nr][nc] != 0 and not visited[nr][nc] : # 범위 안에 있고 빙산이고 방문 안했으면
                visited[nr][nc] = 1 # 방문처리
                q.append((nr, nc))

N, M = map(int, input().rstrip().split()) # 세로 N, 가로 M
iceberg = [list(map(int, input().rstrip().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

# 1. bfs로 분리되었는지 확인
# 2. 분리되어있지 않다면, 각 칸이 올 해에 얼마나 줄어드는지 확인
# 3. 빙산 녹임
# 다시 1로

yr = 0

while True :

    # 1. 분리되어있는지 확인
    visited = [[0] * M for _ in range(N)]
    divCnt = 0
    divided = False
    iceCnt = 0
    for r in range(N) :
        if divided : break # 분리되어있으면 종료
        for c in range(M) :
            if iceberg[r][c] != 0 :
                iceCnt += 1
                if not visited[r][c] : # 빙산이고 아직 방문 안함
                    if divCnt == 0 :
                        bfs(r, c) # 덩어리 방문처리하고 또 방문 안한거 있는지 다시 확인
                        divCnt += 1
                    else : # 덩어리 하나 있는데, 또 덩어리 -> 분리된거니까 끝냄
                        divided = True
                        break

    # 2-1. 분리되었으면 while 종료
    if divided : break
    # 분리되기전에 다 녹았으면 종료
    if iceCnt == 0 :
        yr = 0
        break
    # 2-2. 분리되어있지 않다면, 빙산 얼마나 줄어드는지 확인
    yr += 1
    dcrs = [] #[r, c, 줄어드는 양] 넣을 list

    for r in range(N) :
        for c in range(M) :
            if iceberg[r][c] != 0 : # 빙산이면
                amount = 0 # 인접한거 바다일 때 amount += 1
                if r-1 >= 0 and iceberg[r-1][c] == 0 : amount += 1
                if r+1 < N and iceberg[r+1][c] == 0 : amount += 1
                if c-1 >= 0 and iceberg[r][c-1] == 0 : amount += 1
                if c+1 < M and iceberg[r][c+1] == 0 : amount += 1
                # 줄어드는게 있을 때만 append
                if amount != 0 : dcrs.append([r, c, amount])

    # 3. 빙산 줄이기 (줄일거 있을 때만)
    if len(dcrs) > 0 :
        for cr, cc, amount in dcrs :
            iceberg[cr][cc] -= amount
            if iceberg[cr][cc] < 0 : iceberg[cr][cc] = 0 # 줄였는데 0보다 작으면 0으로

print(yr)

import sys
from collections import deque
input = sys.stdin.readline

def bfs(r, c) :

    tmp = []
    q = deque()
    q.append((r, c))
    tmp.append([r, c, A[r][c]])

    while q :
        cr, cc = q.popleft()
        visited[cr][cc] = True

        # 사방 탐색
        for i in range(4) :
            nr, nc = cr + dr[i], cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] : # 새로운 좌표가 범위 안이고 방문 안함
                gap = abs(A[nr][nc] - A[cr][cc]) # 인구 차이

                if L <= gap <= R : # 인구차이 L 이상 R 이하면
                    # 국경 열기
                    visited[nr][nc] = 1
                    tmp.append([nr, nc, A[nr][nc]])

                    q.append((nr, nc))

    if len(tmp) > 1 : popmove.append(tmp) # 2개 이상의 국가가 국경 열었을 때만 넣음


# input
N, L, R = map(int, input().rstrip().split()) # 땅 크기 NxN, 인구차이 L 이상 R 이하일 때 인구이동
A = [list(map(int, input().rstrip().split())) for _ in range(N)]

#국경을 열 나라 어떻게 찾을지?
# 1) 사방탐색해서 국경을 열 나라 찾기 (bfs) 찾으면 list에 [r, c, 인구] 넣기 & visited true
# 2) 이렇게 모든 칸에 대해 탐색하면 인구이동

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

cnt = 0

while True :
    # 1) bfs로 국경을 열 나라 찾기
    visited = [[0] * N for _ in range(N)]
    popmove = [] # 찾으면 넣을 리스트

    for r in range(N) :
        for c in range(N) :
            if not visited[r][c] : bfs(r, c)

    # 연합 없으면 종료
    if len(popmove) == 0 : break

    # 2) 인구이동
    for move in popmove :
        popcnt = len(move) # 연합을 이루고 있는 칸의 개수
        popsum = 0 # 연합의 인구수
        for i in range(popcnt) : popsum += move[i][2]
        # 따라서 각 칸의 인구수는
        popres = popsum // popcnt # 소수점 버림

        for r, c, pop in move : A[r][c] = popres # 인구수 바꿔줌

    cnt += 1 # 인구이동 +1일

print(cnt)

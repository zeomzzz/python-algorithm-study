import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())  # 세로 N, 가로 M
board = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 돌면서 현재 남은 치즈 조각 수, 녹을 치즈 찾기
# 치즈 녹이기 + 시간 더해줌

cur = 0
time = 0

while True:
    # 0. 구멍 처리 : 0, 0 부터 bfs로 공기 표시(-1)
    visited = [[0] * M for _ in range(N)]

    q = deque()
    q.append((0, 0))
    board[0][0] = -1
    visited[0][0] = 1

    dr = [-1, 1, 0, 0]
    dc = [0, 0, 1, -1]

    while q:
        cr, cc = q.popleft()

        for i in range(4):
            nr, nc = cr + dr[i], cc + dc[i]
            if 0 <= nr < N and 0 <= nc < M and board[nr][nc] < 1 and not visited[nr][nc]:
                board[nr][nc] = -1
                visited[nr][nc] = 1
                q.append((nr, nc))

    # 1. 현재 남은 치즈 조각 수, 녹을 치즈 찾기
    melts = []
    cur = 0

    for r in range(N):
        for c in range(M):
            if board[r][c] == 1:  # 치즈
                cur += 1  # 현재 치즈 조각 + 1
                # 공기와 2면 이상 접촉하면 녹음
                amount = 0
                if r-1 >= 0 and board[r - 1][c] == -1 : amount += 1
                if r+1 < N and board[r + 1][c] == -1 : amount += 1
                if c-1 >= 0 and board[r][c - 1] == -1 : amount += 1
                if c+1 < M and board[r][c + 1] == -1: amount += 1
                if amount >= 2 : melts.append([r, c])

    # 2. 녹을 치즈 있으면 치즈 녹이기
    if cur == 0: break  # 남은 치즈 없으면 끝냄
    if len(melts) > 0:
        time += 1
        for r, c in melts: board[r][c] = 0


print(time)

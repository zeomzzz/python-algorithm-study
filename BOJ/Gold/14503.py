import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 세로 N, 가로 M
r, c, d = map(int, input().rstrip().split()) # d : 0 북, 1 동, 2 남, 3 서
room = [list(map(int, input().rstrip().split())) for _ in range(N)]

dr = [-1, 0, 1, 0] # 전진했을 때, 북, 동, 남, 서
dc = [0, 1, 0, -1]

cnt = 0
q = deque()

q.append((r, c))

while q :
    cr, cc = q.popleft()

    # 현재 칸이 아직 청소되지 않은 경우, 현재 칸을 청소
    if room[cr][cc] == 0 :
        room[cr][cc] = -1
        cnt += 1

    # 90도 씩 돌면서 청소 됐는지 확인하고 다 돌면 후진
    for i in range(1, 5) :
        d = (d - 1) % 4

        nr, nc = cr + dr[d], cc + dc[d] # 다음 위치 정하고

        if 0 <= nr < N and 0 <= nc < M and room[nr][nc] == 0 : # 범위 안에 있고, 청소해야하면
            q.append((nr, nc)) # q에 넣고
            break # 끝냄(청소하기 위해)

        if i == 4 : # 4까지 왔는데도 안 끝났다?
            tmp = (d + 2) % 4 # 후진하는 방향 찾기

            nr, nc = cr + dr[tmp], cc + dc[tmp]

            if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1 : # 범위 안에 있고 벽이 아니면
                q.append((nr, nc)) # q에 넣기 (계속 반복되도록)

print(cnt)

import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip()) # 보드의 크기 N (벽 -1, 사과 1, 뱀 2)

board = [[0] * (N + 2) for _ in range(N + 2)] # 벽 만들기 위해서 N+2
# 벽은 -1로 처리
for i in range(N + 2) :
    board[0][i] = board[N+1][i] = board[i][0] = board[i][N+1] = -1

K = int(input().rstrip()) # 사과의 개수 K
for _ in range(K) :
    r, c = map(int, input().rstrip().split())
    board[r][c] = 1 # 사과

L = int(input().rstrip()) # 뱀의 방향 변환 정보 L
dirs = deque()
for _ in range(L) :
    X, D = input().rstrip().split()
    dirs.append((int(X), D))

dr = [0, 1, 0, -1] # 오른쪽에서 시작. 오른쪽으로 90도씩
dc = [1, 0, -1, 0]

snake = [(1, 1)] # 머리 ~ 꼬리
board[1][1] = 2 # 뱀은 2
d = 0 # 현재 방향
cnt = 0 # 게임 몇 초

while True :
    cnt += 1
    d = d % 4
    cr, cc = snake[0] #현재 머리의 위치

    # 머리를 늘려 다음 칸에 위치
    nr, nc = cr + dr[d], cc + dc[d]
    snake.insert(0, (nr, nc)) # 뱀의 머리에 추가

    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝남
    if board[nr][nc] == -1 or board[nr][nc] == 2 :
        break
    # 만약 이동한 칸에 사과가 있다면, 사과는 없어지고(머리 올리고) 꼬리는 움직이지 않음
    elif board[nr][nc] == 1 :
        board[nr][nc] = 2
    # 이동한 칸에 사과가 없다면 꼬리가 위치한 칸을 비워줌
    else :
        board[nr][nc] = 2 # 뱀 머리 올리고
        tr, tc = snake.pop() # 뱀 길이 줄이고(꼬리 좌표 꺼냄)
        board[tr][tc] = 0 # 꼬리 칸 비워줌

    # X초가 끝나면 방향을 전환
    if len(dirs) > 0 :
        time, dir = dirs[0]
        if time == cnt : # n 초가 되면
            if dir == 'D' : d += 1
            else : d -= 1

            dirs.popleft() # X초 확인하면 pop

print(cnt)

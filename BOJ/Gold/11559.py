import sys
from collections import deque
input = sys.stdin.readline

puyos = [list(input().rstrip()) for _ in range(12)]

# 1. 터지는 뿌요 찾아서 모아두기
# 2. 모인 뿌요 터뜨리기. 이때 위에 있는 뿌요 내려와야 함
# 3. 터뜨릴 뿌요 없으면 종료

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]
cnt = 0

while True :

    puyo_bomb = [] # 터지는 뿌요 모아두기

    # 1. bfs 로 터지는 뿌요 찾기
    visited = [[0] * 6 for _ in range(12)]
    for r in range(12) :
        for c in range(6) :
            if puyos[r][c] != '.' and not visited[r][c] : # 뿌요이고 방문 안했으면
                target = puyos[r][c] # 이 색깔 찾기
                targets = [(r, c)] # 찾은 뿌요 넣기

                # bfs
                q = deque()
                q.append((r, c))
                visited[r][c] = 1

                while q :
                    cr, cc = q.popleft()

                    for i in range(4) :
                        nr, nc = cr + dr[i], cc + dc[i]

                        if 0 <= nr < 12 and 0 <= nc < 6 and puyos[nr][nc] == target and not visited[nr][nc] : # 범위 안에 있고 같은 색이면
                            visited[nr][nc] = 1
                            targets.append((nr, nc)) # 찾은 뿌요 넣어줌
                            q.append((nr, nc))

                if len(targets) >= 4 : # 찾은 뿌요 4개 이상이면
                    puyo_bomb.append(targets) # 터뜨릴 뿌요 세트 모아두기

    # 2. 뿌요 터뜨리기 & 위의 뿌요 떨어뜨리기
    if len(puyo_bomb) == 0 :
        break # 터뜨릴 뿌요 없으면 끝내기

    cnt += 1

    for puyo in puyo_bomb :
        for r, c in puyo :
            puyos[r][c] = '.'

    # 3. 뿌요 증력에 의해 떨어뜨리기
    for r in range(11, -1, -1) :
        for c in range(6) :
            if puyos[r][c] != '.' : # 뿌요
                for i in range(r+1, 12) : # 어디까지 떨어져야하는지 찾기
                    if puyos[i][c] == '.' : # 떨어질 공간 있음
                        if (i+1 < 12 and puyos[i+1][c] != '.') or i+1 == 12 : #
                            puyos[i][c] = puyos[r][c]
                            puyos[r][c] = '.'
                            break

print(cnt)

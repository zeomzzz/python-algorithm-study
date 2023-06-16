import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip()) # 공간의 크기 N*N
area = [list(map(int, input().rstrip().split())) for _ in range(N)]

sr, sc, size = 0, 0, 2
for r in range(N) :
    for c in range(N) :
        if area[r][c] == 9 :
            sr, sc = r, c
area[sr][sc] = 0

dr = [-1, 0, 0, 1] # 상, 좌, 우, 하
dc = [0, -1, 1, 0]

sec = 0
ate = 0

q = deque()
q.append((sr, sc))

# 다음 위치 구하기 위한 bfs
def eat(cr, cc, size) :
    visited = [[0] * N for _ in range(N)]
    tmp = [] # 먹을 수 있는 물고기 담자
    flag = True

    q = deque()
    q.append((cr, cc))

    while q :
        cr, cc = q.popleft()

        for i in range(4) :
            nr, nc = cr + dr[i], cc + dc[i]

            if 0 <= nr < N and 0 <= nc < N and area[nr][nc] <= size and not visited[nr][nc] :
                visited[nr][nc] = visited[cr][cc] + 1

                # 그냥 이동
                if area[nr][nc] == size or area[nr][nc] == 0 :
                    q.append((nr, nc)) # 다음 단계를 위해 q에 넣기

                # 먹을 수 있는 물고기
                else :
                    if len(tmp) != 0 and visited[nr][nc] != tmp[0][2] : # 지금 들어있는거 있는데 거리가 다르면(다음 수준으로 넘어간 것)
                        flag = False
                        break

                    tmp.append([nr, nc, visited[nr][nc]])  # r, c, distance

        if not flag : break

    return sorted(tmp, key=lambda x: (x[0], x[1]))


# 상어 이동
sec = 0
ate = 0
while True :

    eat_lst = eat(sr, sc, size)

    if len(eat_lst) == 0 : break # 먹을거 없으면 끝내
    else :
        sr, sc = eat_lst[0][0], eat_lst[0][1] # 다음 출발지
        sec += eat_lst[0][2] # 시간

        area[sr][sc] = 0 # 먹었음
        ate += 1

        if ate == size :
            size += 1
            ate = 0

print(sec)

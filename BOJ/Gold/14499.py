import sys
input = sys.stdin.readline

# input
N, M, x, y, K = map(int, input().rstrip().split()) # 지도 세로 N, 가로 M, 주사위 좌표 x(세로), y(가로), 명령 개수 K
maps = [list(map(int, input().rstrip().split())) for _ in range(N)]
orders = list(map(int, input().rstrip().split())) # 동 1, 서 2, 북 3, 남 4

dice = [0] * 7 # 1번 인덱스에 1이 오도록

cr, cc = x, y
dr = [0, 0, 0, -1, 1] # 1부터 동, 서, 북, 남
dc = [0, 1, -1, 0, 0]

for order in orders :
    nr, nc = cr + dr[order], cc + dc[order]

    if nr < 0 or nr >= N or nc < 0 or nc >= M : # 범위 밖이면 continue
        continue

    # 1) 범위 안이면 현재 위치 바꿔줌
    cr, cc = nr, nc

    # 2) 주사위 굴리기
    match(order) :
        case 1: # 동
            dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
        case 2: # 서
            dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
        case 3: # 북
            dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
        case 4: # 남

            dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]


    # 3) 이동한 칸의 값에 따라 값 복사 (주사위 바닥 : dice[6])
    if maps[cr][cc] == 0 : maps[cr][cc] = dice[6]
    else :
        dice[6] = maps[cr][cc]
        maps[cr][cc] = 0

    # 4) dice[1] 출력
    print(dice[1])

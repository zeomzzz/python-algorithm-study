import sys
input = sys.stdin.readline

# 1. 지도에 로봇 올리기. 이때, 로봇 번호 확인을 위해 로봇 위치를 robots에 담아두기
# 2. 명령 입력 받기
# 3. 명령 횟수 만큼 반복
# 4. 마지막까지 while 반복되면 OK, 그렇지 않은 경우 답 출력

A, B = map(int, input().rstrip().split()) # 가로 A, 세로 B
N, M = map(int, input().rstrip().split()) # 로봇 N개 (1~N), 명령 M개

ground = [[0] * A for _ in range(B)]
robots = [[-1, -1]]
for i in range(N) :
    x, y, dir = input().rstrip().split()

    x, y = int(x) - 1, abs(int(y) - B)

    match dir : # dr, dc를 idx로 찾도록
        case 'N' : dir = 0
        case 'E' : dir = 1
        case 'S' : dir = 2
        case 'W' : dir = 3

    ground[y][x] = i + 1
    robots.append([y, x, dir])

dr = [-1, 0, 1, 0] # N, E, S, W
dc = [0, 1, 0, -1]

flag = True
X, Y = 0, 0 # 움직이는 로봇 X, 충돌 당한 로봇 Y

for _ in range(M) :
    robot, order, cnt = input().rstrip().split()
    robot, cnt = int(robot), int(cnt)

    # 명령 수행
    match order :
        case 'L' : # 왼쪽으로 90도
            robots[robot][2] -= cnt

        case 'R' : # 오른쪽으로 90도
            robots[robot][2] += cnt

        case 'F' :
            for c in range(cnt) :
                dir = robots[robot][2] % 4
                cr, cc = robots[robot][0], robots[robot][1]
                nr, nc = cr + dr[dir], cc + dc[dir]

                # 충돌 체크
                # 벽과 충돌
                if nr < 0 or nr >= B or nc < 0 or nc >= A : # 범위 밖이면
                    X = robot
                    flag = False
                    break

                # 범위 안인데 다른 로봇과 충돌
                elif ground[nr][nc] != 0 : # 한 칸 갔는데 로봇이 아님
                    X = robot
                    Y = ground[nr][nc]
                    flag = False
                    break

                # 정상 실행
                else :
                    # 로봇 이동
                    ground[cr][cc] = 0
                    ground[nr][nc] = robot
                    robots[robot][0], robots[robot][1] = nr, nc

    if not flag : break

if flag : print('OK')
else :
    if Y == 0 :
        print('Robot ' + str(X) + ' crashes into the wall')
    else :
        print('Robot ' + str(X) + ' crashes into robot ' + str(Y))

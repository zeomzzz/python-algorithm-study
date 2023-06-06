import sys
input = sys.stdin.readline

saw = [list(map(int, input().rstrip())) for _ in range(4)]
saw.insert(0, [0, 0, 0, 0, 0, 0, 0, 0]) # 문제에서 첫번째가 1번이어서 헷갈리지 않도록
# saw.append([0, 0, 0, 0, 0, 0, 0, 0])

K = int(input().rstrip()) # 회전횟수 K

# 맞닿는 톱니 : 6과 2, 2와 6
# 1 : 시계 방향, -1 : 반시계 방향
for _ in range(K) :
    sawNum, dir = map(int, input().rstrip().split())

    # 1. 회전 방향을 정해주기
    dirs = [2, 2, 2, 2, 2]
    dirs[sawNum] = dir
    for i in range(1, 4) :
        # 내 오른쪽 톱니
        if sawNum + i < 5 and dirs[sawNum + i] == 2 : # 범위 안이고 아직 안 정함
            if dirs[sawNum + i - 1] == 0:  # 이전 톱니가 회전을 안함
                dirs[sawNum + i] = 0 # 나도 회전 안함
            else : # 이전 톱니 회전 함
                if saw[sawNum + i - 1][2] == saw[sawNum + i][6] : # 같으면
                    dirs[sawNum + i] = 0 # 회전 안함
                else : # 다르면
                    dirs[sawNum + i] = dirs[sawNum + i - 1] * (-1) # 반대 방향으로 회전

        # 내 왼쪽 톱니
        if sawNum - i > 0 and dirs[sawNum - i] == 2 : # 범위 안이고 아직 안정함
            if dirs[sawNum - i + 1] == 0 : # 이전 톱니가 회전을 안함
                dirs[sawNum - i] = 0 # 나도 회전 안함
            else :
                if saw[sawNum - i + 1][6] == saw[sawNum - i][2] : # 같으면
                    dirs[sawNum - i] = 0 # 회전 안함
                else :
                    dirs[sawNum - i] = dirs[sawNum - i + 1] * (-1) # 반대 방향으로 회전

    # 2) 톱니 회전
    for i in range(1, 5) :
        if dirs[i] == 0 :
            continue
        elif dirs[i] == 1 : # 시계 방향
            saw[i].insert(0, saw[i].pop()) # 맨 뒤 것을 맨 앞에
        else: # 반시계 방향
            tmp = saw[i][0]
            del saw[i][0]
            saw[i].append(tmp) # 맨 앞의 것을 맨 뒤에

ans = 0
for i in range(1, 5) :
    if saw[i][0] == 0 :
        continue
    else :
        ans += 2 ** (i - 1)

print(ans)

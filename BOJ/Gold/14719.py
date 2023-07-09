# 풀이 1
import sys
input = sys.stdin.readline

H, W = map(int, input().rstrip().split()) # 세로 H, 가로 W
blocks = list(map(int, input().rstrip().split()))

# 각 칸에 빗물 고여도 되나? 를 확인
# 조건 : 왼쪽에 벽 or 빗물 + 오른쪽 어딘가에 나보다 높은 블럭 있음
water = 0

for i in range(1, W - 1) :
    flag = True

    while flag :
        if blocks[i - 1] > blocks[i] and i + 1 < W :
            for j in range(i + 1, W) :
                if blocks[i] < blocks[j] :
                    water += 1
                    blocks[i] += 1
                    break
                elif j == W - 1 : flag = False
        else : flag = False

print(water)


# 풀이 2

import sys
input = sys.stdin.readline

H, W = map(int, input().rstrip().split()) # 세로 H, 가로 W
blocks = list(map(int, input().rstrip().split()))

# i번째 블럭에 빗물 고이는 양
# i 이전 블럭 최대 높이, 이후 블럭 최대 높이 중 낮은 블럭과 현재 블럭의 차이 만큼

rain = 0

for i in range(1, W - 1) :
    left = max(blocks[:i])
    right = max(blocks[i:])

    tmp = min(left, right)

    if tmp > blocks[i] : rain += tmp - blocks[i]

print(rain)

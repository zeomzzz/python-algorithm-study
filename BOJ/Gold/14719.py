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

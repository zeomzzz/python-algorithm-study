import sys
input = sys.stdin.readline

n = int(input())
paint = [[0, 0, 0]] # R, G, B

for _ in range(n) :
    tmp = list(map(int, input().rstrip().split()))
    paint.append(tmp)

for i in range(2, n + 1) :
    # n R : min(n-1 G, n-1 B) + n R
    paint[i][0] += min(paint[i - 1][1], paint[i - 1][2])

    # n G : min(n-1 R, n-1 B) + n G
    paint[i][1] += min(paint[i - 1][0], paint[i - 1][2])

    # n B : min(n-1 R, n-1 G) + n B
    paint[i][2] += min(paint[i - 1][0], paint[i - 1][1])

print(min(paint[-1]))

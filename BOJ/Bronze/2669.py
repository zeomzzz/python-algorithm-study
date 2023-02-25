import sys

lst = [[False] * 101 for _ in range(101)]

for _ in range(4) :
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())

    for r in range(x1, x2) :
        for c in range(y1, y2) :
            lst[r][c] = True

cnt = 0
for r in range(1, 101) :
    for c in range(1, 101) :
        if lst[r][c] == True :
            cnt += 1

print(cnt)

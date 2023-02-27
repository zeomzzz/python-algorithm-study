import sys

n = int(sys.stdin.readline().rstrip())

paper = [[0] * 100 for _ in range(100)]

for _ in range(n) :
    a, b = map(int, sys.stdin.readline().rstrip().split())

    for r in range(a, a + 10) :
        for c in range(b, b + 10) :
            paper[r][c] = 1

sum = 0
for i in range(100) :
    for j in range(100) :
        sum += paper[i][j]

print(sum)

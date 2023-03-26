import sys
input = sys.stdin.readline

n = int(input())
tri = [list(map(int, input().split())) for _ in range(n)]
for i in range(n) :
    tri[i].insert(0, 0)
    tri[i].append(0)

for i in range(1, n) : # 2번째줄부터 n번째 줄까지
    for j in range(1, i + 2) :
        tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

print(max(tri[n - 1]))

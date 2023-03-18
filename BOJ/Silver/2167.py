import sys
input = sys.stdin.readline

n, m = map(int, input().split())

sum_lst = [[0] for _ in range(n)]

for i in range(n) :
    sum_lst[i] = list(map(int, input().split()))
    sum_lst[i].insert(0, 0)

sum_lst.insert(0, [0] * (m + 1))

for i in range(1, n + 1) :
    for k in range(1, m + 1) :
        sum_lst[i][k] += sum_lst[i - 1][k] + sum_lst[i][k - 1] - sum_lst[i - 1][k - 1]

t = int(input())
for _ in range(t) :
    i, j, x, y = map(int, input().split())
    print(sum_lst[x][y] - sum_lst[i - 1][y] - sum_lst[x][j - 1] + sum_lst[i - 1][j - 1])

import sys
input = sys.stdin.readline

N = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
ans = 0
cnt = 0

# make set
p = [i for i in range(N)]

# findset
def findset(x) :
    if x != p[x] :
        p[x] = findset(p[x])
    return p[x]

# union
def union(x, y) :
    p[findset(y)] = findset(x)

edges = []

for i in range(N - 1) :
    for j in range(i + 1, N) :
        edges.append((graph[i][j], i, j))

edges.sort()

for edge in edges :
    w, x, y = edge

    if findset(x) != findset(y) :
        union(x, y)
        ans += w
        cnt += 1

        if cnt == N - 1 : break

print(ans)

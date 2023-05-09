import sys
input = sys.stdin.readline

n = int(input().rstrip()) # 별의 개수 n

p = [0] * (n + 1)
for i in range(1, n + 1) :
    p[i] = i

def distance(a, b) :
    return ((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2) ** (1 / 2)

def findset(x) :
    if x != p[x] :
        p[x] = findset(p[x])
    return p[x]

def union(x, y) :
    p[findset(y)] = findset(x)

nodes = []
edges = []
for _ in range(n) :
    nodes.append(list(map(float, input().rstrip().split())))

for i in range(n - 1) :
    a = nodes[i]
    for j in range(i + 1, n) :
        b = nodes[j]
        edges.append((distance(a, b), i, j))

edges.sort()

res = 0

for w, x, y in edges :

    # x, y 같은 집합 아니면
    if findset(x) != findset(y) :
        # 합치고
        union(x, y)
        # 정답에 추가
        res += w

print(round(res, 2))

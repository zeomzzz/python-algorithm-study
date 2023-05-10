import sys
input = sys.stdin.readline

def findset(x) :
    if x != p[x] :
        p[x] = findset(p[x])
    return p[x]

def union(x, y) :
    p[findset(y)] = findset(x)

while True :
    m, n = map(int, input().rstrip().split())

    if (m, n) == (0, 0) : break

    edges = []
    total = 0
    p = [i for i in range(m)]

    for _ in range(n) :
        x, y, z = map(int, input().rstrip().split())
        edges.append((z, x, y))
        total += z

    edges.sort()

    for edge in edges :
        z, x, y = edge

        # x, y가 같은 집합이 아니면
        if findset(x) != findset(y) :
            # 합치고
            union(x, y)
            total -= z

    print(total)

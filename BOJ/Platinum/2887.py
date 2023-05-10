import sys
input = sys.stdin.readline

N = int(input().rstrip())
nodes = []
edges = []
ans = 0
cnt = 0

# make set
p = [i for i in range(N)]

# findset
def findset(x) :
    if x != p[x] :
        p[x] = findset(p[x])
    return p[x]

def distance(a, b) :
    return min([abs(a[0] - b[0]), abs(a[1] - b[1]), abs(a[2] - b[2])])

for i in range(N) :
    x, y, z = map(int, input().rstrip().split())
    nodes.append([x, y, z, i])

for i in range(3) :
    nodes.sort(key = lambda x:x[i])

    for j in range(N - 1) :
        edges.append((distance(nodes[j], nodes[j + 1]), nodes[j][3], nodes[j + 1][3]))

edges.sort()

for edge in edges :
    d, x, y = edge

    # x, y 가 같은 집합이 아니면
    if findset(x) != findset(y) :
        p[findset(y)] = findset(x)
        ans += d
        cnt += 1

        if cnt == N - 1 :
            break

print(ans)

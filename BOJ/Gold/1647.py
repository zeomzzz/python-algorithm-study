import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

def findset(x):
    if p[x] != x :
        p[x] = findset(p[x])
    return p[x]

n, m = map(int, input().split()) # 집의 개수 n, 길의 개수 m
nodes = [list(map(int, input().split())) for _ in range(m)]

# 1. 비용에 따라 정렬
nodes = sorted(nodes, key = lambda x : x[2])

# 2. make set
p = [x for x in range(n + 1)]

# 같은 집합 아니면 합치기
pick = 0
ans = 0

for h1, h2, cost in nodes :
    px = findset(h1)
    py = findset(h2)

    if px != py :
        p[py] = px
        pick += 1
        ans += cost

    if pick == n - 2 : break # 분리되어야 하므로 가중치 가장 큰 것만 빼고 구함

print(ans)

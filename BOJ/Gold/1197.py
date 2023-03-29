import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 4)

def findset(x):
    if p[x] != x :
        p[x] = findset(p[x])
    return p[x]

v, e = map(int, input().split()) # 정점의 개수 v, 간선의 개수 e
nodes = [list(map(int, input().split())) for _ in range(e)] # 정점 a, b, 가중치 c

# 1. 가중치에 따라 정렬
nodes = sorted(nodes, key=lambda x : x[2])

# 2. make-set
p = [i for i in range(v+1)]

pick = 0
min = 0

for x, y, w in nodes :
    px = findset(x)
    py = findset(y)

    # 같은 집합 아니면 합치기
    if px != py :
        p[py] = px
        min += w
        pick += 1

    if pick == v - 1 : break

print(min)

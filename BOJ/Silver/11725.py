import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())

tree = [[] for _ in range(n + 1)]
for _ in range(n - 1) :
    a, b = map(int, sys.stdin.readline().rstrip().split())
    tree[a].append(b)
    tree[b].append(a)

parent = [0] * (n + 1)


def dfs(v) :
    for i in tree[v] :
        if not parent[i] :
            parent[i] = v # i의 부모가 v
            dfs(i)

dfs(1)
for i in range(2, n + 1) : # index 1 에 1의 부모가 들어가는데, 1이 루트 노드이므로 2부터 출력
    print(parent[i])

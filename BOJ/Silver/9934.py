import sys

# 트리 중위 순회의 결과 -> 트리로

k = int(sys.stdin.readline().rstrip())

# 1번 인덱스부터 활용하기 위해
visited = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
tree_idx = [[] for _ in range(k + 1)]

# 각 레벨 별로 가지고 있는 노드의 번호를 담음
tree_idx[1].append(2 ** (k - 1))

for i in range(2, k + 1) :
    for idx in tree_idx[i - 1] :
        tree_idx[i].append(idx - 2 ** (k - i))
        tree_idx[i].append(idx + 2 ** (k - i))

# 노드 번호를 인덱스로 활용하여 출력
for i in range(1, k + 1) :
    for idx in tree_idx[i] :
        print(visited[idx], end = ' ')
    print()

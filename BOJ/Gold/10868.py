import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split()) # 수 N개, M개 최소값 구하기

# 1. 트리의 크기 구하기
k = 1
while True :
    if 2 ** k >= N : break
    k += 1

tree_size = (2 ** k) * 2
tree = [sys.maxsize] * tree_size

# 2. 트리에 수를 채우기
leaf_start = 2 ** k

for i in range(N) : tree[leaf_start + i] = int(input().rstrip())
for i in range(leaf_start - 1, 0, -1) : tree[i] = min(tree[2 * i], tree[2 * i + 1])

for i in range(M) :
    ans = sys.maxsize
    a, b = map(int, input().rstrip().split())
    start_index, end_index = a + leaf_start - 1, b + leaf_start - 1

    while start_index <= end_index :
        if start_index % 2 == 1 : ans = min(tree[start_index], ans)
        if end_index % 2 == 0 : ans = min(tree[end_index], ans)

        start_index = (start_index + 1) // 2
        end_index = (end_index - 1) // 2

    print(ans)

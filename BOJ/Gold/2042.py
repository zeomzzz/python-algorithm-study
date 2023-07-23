import sys
input = sys.stdin.readline

N, M, K = map(int, input().rstrip().split()) # 수의 개수 N, 변경 횟수 M, 구간 합 구하기 K회

# 1. 세그먼트 트리의 크기 구하기
# 1-1. k 구하기
k = 1
while True :
    if 2 ** k >= N : break
    k += 1

# 1-2. 트리의 크기 구하기
tree_size = (2 ** k) * 2

tree = [0] * tree_size

# 2. 트리 리프 노드에 값 채우기
leaf_start = 2 ** k

for i in range(N) : tree[leaf_start + i] = int(input().rstrip())

# 3. 리프 노드 외의 노드 채우기
for i in range(leaf_start - 1, 0, -1) : tree[i] = tree[i * 2] + tree[i * 2 + 1]

for i in range(M + K) :
    a, b, c = map(int, input().rstrip().split())

    match a :
        case 1 : # 업데이트
            b = leaf_start + b - 1
            tree[b] = c

            while True :
                b = b // 2

                if b < 1 : break

                tree[b] = tree[b * 2] + tree[b * 2 + 1]

        case 2 : # 구간합
            start_index, end_index = b + leaf_start - 1, c + leaf_start - 1
            ans = 0

            while True :
                if start_index % 2 == 1 : ans += tree[start_index]
                if end_index % 2 == 0 : ans += tree[end_index]

                start_index = (start_index + 1) // 2
                end_index = (end_index - 1) // 2

                if end_index < start_index : break

            print(ans)

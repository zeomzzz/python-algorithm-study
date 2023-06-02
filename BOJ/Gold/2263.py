import sys
input = sys.stdin.readline

sys.setrecursionlimit(10 ** 6)

n = int(input().rstrip())
inorder = list(map(int, input().rstrip().split()))
postorder = list(map(int, input().rstrip().split()))
idx_lst = [0] * (n + 1)
for i in range(n): idx_lst[inorder[i]] = i

# post에서 root를 찾고
# in에서 반띵해서 다음 트리 찾기

def traverse(in_start, in_end, post_start, post_end) :

    if in_start > in_end or post_start > post_end :
        return

    root = postorder[post_end]

    print(root, end = " ")
    idx = idx_lst[root]

    # 1. 좌
    traverse(in_start, idx - 1, post_start, post_start + idx - 1 - in_start)

    # 2. 우
    traverse(idx + 1, in_end, post_start + idx - in_start, post_end - 1)

traverse(0, n - 1, 0, n - 1)

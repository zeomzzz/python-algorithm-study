import sys

n = int(sys.stdin.readline().rstrip())

tree = [[0, 0] for _ in range((ord('Z') - ord('A') + 1))]
# print(tree)
for _ in range(n) :
    root, left, right = sys.stdin.readline().rstrip().split()
    root_idx = ord(root) - ord('A')
    tree[root_idx][0] = left
    tree[root_idx][1] = right

def tree_pre(tree, root) :
    root_idx = ord(root) - ord('A')

    if root != '.' : # 순회하다가 . 만나면 그 순회는 종료되고 다음으로 감
        print(root, end = '') # 루트 출력
        tree_pre(tree, tree[root_idx][0]) # 왼쪽 순회
        tree_pre(tree, tree[root_idx][1])# 오른쪽 순회


def tree_in(tree, root) :
    root_idx = ord(root) - ord('A')

    if root != '.' :
        tree_in(tree, tree[root_idx][0])
        print(root, end = '')
        tree_in(tree, tree[root_idx][1])


def tree_post(tree, root) :
    root_idx = ord(root) - ord('A')

    if root != '.' :
        tree_post(tree, tree[root_idx][0])
        tree_post(tree, tree[root_idx][1])
        print(root, end = '')


tree_pre(tree, "A")
print()
tree_in(tree, "A")
print()
tree_post(tree, "A")

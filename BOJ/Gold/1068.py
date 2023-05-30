import sys
from collections import deque
input = sys.stdin.readline

n = int(input().rstrip())
tree = list(map(int, input().rstrip().split()))
visited = [0] * n

node = int(input().rstrip())  # 지우는 노드

q = deque()
q.append(node)

# 지우는 노드 포함 아래는 다 제거
while q :
    cur = q.popleft()
    tree[cur] = -2
    visited[cur] = 1

    for i in range(n) :
        if tree[i] == cur and not visited[i] :
            q.append(i)

root = 0
for i in range(n) :
    if tree[i] == -1 :
        root = i
        break

q = deque()
q.append(root)

while q :
    cur = q.popleft()

    for i in range(n) :
        if tree[i] == cur and not visited[i] :
            visited[cur] = 1
            q.append(i)

print(n - sum(visited))

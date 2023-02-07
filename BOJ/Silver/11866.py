import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
ans = ""

lst = []
for i in range(1, n + 1) :
    lst.append(i)

dq = deque(lst)

while len(dq) > 0 :
    for i in range(k - 1) :
        dq.append(dq.popleft())

    ans += str(dq.popleft()) + ", "

ans = "<" + ans[:-2] + ">"

print(ans)

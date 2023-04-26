from collections import deque
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())

q = [i for i in range(1, N + 1)]
q = deque(q)
cnt = 1
ans = '<'

while q :
    if cnt != K :
        q.append(q.popleft())
        cnt += 1
    else :
        ans += str(q.popleft())
        ans += ', '
        cnt = 1

ans = ans[:-2] + '>'
print(ans)

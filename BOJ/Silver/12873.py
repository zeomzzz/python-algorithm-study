import sys
from collections import deque
input = sys.stdin.readline

N = int(input().rstrip())

q = []
for i in range(1, N + 1) : q.append(i)

ans = 0

start = 0
tmp = 0

for i in range(1, N) :
    cnt = (i ** 3) % len(q)

    tmp = (start + cnt - 1) % len(q)
    if tmp < 0 :
        tmp += len(q)
    q.pop(tmp)
    start = tmp

print(q[0])

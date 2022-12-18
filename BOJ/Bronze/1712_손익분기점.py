# 풀이 1

import math

A, B, C = map(int, input().split())


if C == B :
    n = -1
else :
    n = math.floor(A / (C - B)) + 1

if n < 0 :
    print(-1)
else :
    print(n)


# 풀이 2

A, B, C = map(int, input().split())

if B >= C :
    print(-1)
else :
    print(int(A / (C - B)) + 1)

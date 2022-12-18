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

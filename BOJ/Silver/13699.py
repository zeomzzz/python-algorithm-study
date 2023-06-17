import sys
input = sys.stdin.readline

n = int(input().rstrip())
t = [0] * (n + 1)
if n >= 0 : t[0] = 1
if n >= 1 : t[1] = 1

if n >= 2 :
    for i in range(2, n + 1) :
        for j in range(i) :
            t[i] += t[j] * t[i - 1 - j]

print(t[n])

import sys

n = int(sys.stdin.readline().rstrip())
stairs = [int(sys.stdin.readline().rstrip()) for _ in range(n)]
stairs.insert(0, 0)

scores = [0] * (n + 1)
scores[1] = stairs[1]
if n > 1 : scores[2] = stairs[1] + stairs[2]
if n > 2 : scores[3] = max(stairs[1] + stairs[3], stairs[2] + stairs[3])

if n > 3 :
    for i in range(4, n + 1) :
        scores[i] = max(scores[i - 3] + stairs[i - 1], scores[i - 2]) + stairs[i]

print(scores[n])

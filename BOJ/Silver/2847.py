import sys
input = sys.stdin.readline

N = int(input().rstrip())
scores = []
for i in range(N) : scores.append(int(input().rstrip()))

scores.reverse()

cnt = 0
for i in range(1, N) :
    while scores[i] >= scores[i - 1] :
        cnt += 1
        scores[i] -= 1

print(cnt)

import sys
input = sys.stdin.readline

scores = []
for i in range(1, 9) :
    scores.append((int(input().rstrip()), i))

scores.sort(reverse = True)

ans = []
total = 0
for i in range(5) :
    a, b = scores[i]
    total += a
    ans.append(b)

ans.sort()

print(total)
print(*ans)

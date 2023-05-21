import sys
input = sys.stdin.readline

n, target = map(int, input().rstrip().split())
target = str(target)

ans = 0
for i in range(1, n + 1) :
    tmp = str(i)

    for t in tmp :
        if t == target :
            ans += 1

print(ans)

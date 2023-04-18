import sys
input = sys.stdin.readline

lst = [input().rstrip() for _ in range(5)]

ans = ''

for c in range(15) :
    for r in range(5) :
        if c < len(lst[r]) :
            ans += lst[r][c]

print(ans)

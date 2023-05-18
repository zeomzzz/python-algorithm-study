import sys
input = sys.stdin.readline

ans = 0
for _ in range(5) :
    x = int(input().rstrip())
    if x > 40 : ans += x / 5
    else : ans += 8

print(int(ans))

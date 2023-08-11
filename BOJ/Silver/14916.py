import sys
input = sys.stdin.readline

n = int(input().rstrip())
cnt = 0

if n == 1 or n == 3 : cnt = -1
elif (n % 5) % 2 == 0 :
    cnt += n // 5
    n = n % 5
    cnt += n // 2
else :
    a = n // 5
    cnt += a - 1
    n -= (a - 1) * 5

    if n % 2 == 1 : cnt = -1
    else : cnt += n // 2

print(cnt)

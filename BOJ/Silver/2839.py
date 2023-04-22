import sys
input = sys.stdin.readline

N = int(input().rstrip())
cnt = 0

while N > 0 :
    if N % 5 == 0 :
        cnt += N // 5
        N = 0
    else :
        N -= 3
        cnt += 1

    if N < 0 :
        cnt = -1
        break

print(cnt)

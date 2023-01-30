import sys

N = int(sys.stdin.readline())
lst = list(map(int, sys.stdin.readline().split()))
X = int(sys.stdin.readline())

lst = sorted(lst)
cnt = 0
left = 0
right = N - 1

while left < right :
    if lst[left] + lst[right] == X :
        cnt += 1
        left += 1
        right -= 1
    elif lst[left] + lst[right] < X :
        left += 1
    else :
        right -= 1

print(cnt)

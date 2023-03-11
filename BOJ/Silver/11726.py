import sys

n = int(sys.stdin.readline().rstrip())

lst = [1 for _ in range(n + 1)] # 계산의 편의를 위해 index 0 도 1로 초기화

if n > 1 :
    for i in range(2, n + 1) :
        lst[i] = (lst[i - 1] + lst[i - 2]) % 10007

print(lst[n])

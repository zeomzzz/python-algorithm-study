import sys

n = int(sys.stdin.readline().rstrip())

lst = [1] * (n + 1) # 계산의 편의를 위해 index 0일 때도 1로 초기화

# 규칙 : n번째는 f(n-1) * 1 + f(n-2) * 2
# 마지막 타일의 가로 1일 경우 한 가지
# 마지막 타일의 가로가 2인 경우 두 가지

if n > 1 :
    for i in range(2, n + 1) :
        lst[i] = (lst[i - 1] + lst[i - 2] * 2) % 10007

print(lst[n])

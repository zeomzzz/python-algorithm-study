import sys

k, n = map(int, sys.stdin.readline().rstrip().split())

# 이미 가지고 있는 랜선의 길이를 k_lst에 저장
k_lst = []

for i in range(k) :
    kk = int(sys.stdin.readline().rstrip())
    k_lst.append(kk)

# 첫번째 기준이 되는 값 구함 : k_lst의 합 / (n-k) or k_lst의 최대값
k_lst.sort()

end = max(int(sum(k_lst)/n), k_lst[0])
start = 1

# 이분탐색으로 N개를 만들 수 있는 길이를 구함
while end >= start :

    mid = (start + end) // 2

    sum = 0
    for i in k_lst :
        sum += i // mid

    if sum >= n : # n개 또는 n개보다 많이 만들어야 함
        ans = mid
        start = mid + 1 # 더 긴 길이로 만들 수 있는지 확인
    else :
        end = mid - 1

print(ans)

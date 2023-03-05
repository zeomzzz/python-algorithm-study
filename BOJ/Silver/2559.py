import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
# n : 온도를 측정한 전체 날짜의 수
# k : 합을 구하기 위한 연속적인 날짜의 수
temperature = list(map(int, sys.stdin.readline().rstrip().split())) # 매일 측정한 온도

max_sum = 0
for i in range(k) :
    max_sum += temperature[i]
tmp_sum = max_sum

for i in range(n - k) :
    tmp_sum = tmp_sum - temperature[i] + temperature[i + k]
    if tmp_sum > max_sum : max_sum = tmp_sum

print(max_sum)

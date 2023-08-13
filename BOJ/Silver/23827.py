import sys
input = sys.stdin.readline

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
sum_a = sum(A)

total = 0
for i in range(N - 1) :
    sum_a -= A[i]
    total += sum_a * A[i]

print(total % 1000000007)

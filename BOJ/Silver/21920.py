import sys
input = sys.stdin.readline
import math

N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
X = int(input().rstrip())

total, cnt = 0, 0
for i in A:
    if math.gcd(i, X) == 1:
        total += i
        cnt += 1

print(total/cnt)

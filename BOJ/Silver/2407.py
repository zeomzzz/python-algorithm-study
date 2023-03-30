import sys
input = sys.stdin.readline

n, m = map(int, input().split()) # nCm

a = 1
b = 1

for i in range(n, n-m, -1) :
    a *= i

for i in range(1, m + 1) :
    b *= i

print(a//b)

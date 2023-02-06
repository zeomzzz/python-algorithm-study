import sys

n, m = map(int, sys.stdin.readline().rstrip().split()) # 돈, 생명체 수

print(n // m)
print(n % m)

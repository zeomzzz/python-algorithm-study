import sys

n = int(sys.stdin.readline())
i = 0

while i < n :
    A, B = map(int, sys.stdin.readline().split())
    print(A + B)
    i += 1

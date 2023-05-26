import sys
input = sys.stdin.readline

n = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
lst.sort()

print(*lst)

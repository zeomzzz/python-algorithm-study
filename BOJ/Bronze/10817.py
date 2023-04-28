import sys
input = sys.stdin.readline

lst = list(map(int, input().rstrip().split()))
lst.sort()

print(lst[1])

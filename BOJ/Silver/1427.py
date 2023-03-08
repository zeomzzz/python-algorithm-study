import sys

lst = list(map(int, sys.stdin.readline().rstrip()[:]))
lst.sort(reverse=True)

print(*lst, sep = "")

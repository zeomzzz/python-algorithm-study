import sys

n = int(sys.stdin.readline().rstrip())
lst = []
for _ in range(n) :
    lst.append(int(sys.stdin.readline().rstrip()))

lst.sort(reverse = True)

print(*lst, sep = "\n")

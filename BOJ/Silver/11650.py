import sys

n = int(sys.stdin.readline().rstrip()) # 점 n개

lst = []
for _ in range(n) :
    line = list(map(int, sys.stdin.readline().rstrip().split()))
    lst.append(line)

lst.sort()

for i in lst :
    print(*i)

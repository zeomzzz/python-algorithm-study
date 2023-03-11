import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
lst = list(map(int, sys.stdin.readline().rstrip().split()))
for i in range(1, n) :
    lst[i] += lst[i - 1]
lst.insert(0, 0) # 1번째가 index 1 이 되도록 0 insert

for _ in range(m) :
    i, j = map(int, sys.stdin.readline().rstrip().split())

    print(lst[j] - lst[i - 1])

import sys
input = sys.stdin.readline

N = int(input().rstrip())

lst = []

for _ in range(N) :
    x, y = map(int, input().rstrip().split())

    lst.append([y, x])

lst.sort()

for y, x in lst : print(str(x) + " " + str(y))

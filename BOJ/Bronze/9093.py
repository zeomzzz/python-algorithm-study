import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T) :
    tmp = list(input().rstrip().split(" "))

    for t in tmp :
        print(t[::-1], end = " ")
    print()

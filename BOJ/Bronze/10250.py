import sys

t = int(sys.stdin.readline().rstrip())

for _ in range(t) :
    h, w, n = map(int, sys.stdin.readline().rstrip().split())

    floor = n % h
    room = n // h + 1

    if floor == 0 :
        floor = h
        room -= 1


    print(floor * 100 + room)

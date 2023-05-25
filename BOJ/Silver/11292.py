import sys
input = sys.stdin.readline

while True :
    n = int(input().rstrip())

    if n == 0 : break

    ans = []

    highest = 0

    for i in range(n) :
        name, height = input().rstrip().split()
        height = float(height)

        if height > highest :
            highest = height
            ans = [name]
        elif height == highest :
            ans.append(name)

    print(*ans)

n = int(input())

i = 0

while i < n :
    x, y = map(int, input().split())
    print("Case #" + str(i + 1) + ": " + str(x + y))
    i += 1

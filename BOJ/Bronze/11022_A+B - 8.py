# 풀이 1

n = int(input())

i = 0

while i < n :
    x, y = map(int, input().split())
    print("Case #" + str(i + 1) + ": " + str(x) + " + " + str(y) + " = " + str(x + y))
    i += 1


# 풀이 2

n = int(input())

i = 0

while i < n :
    x, y = map(int, input().split())
    print(f'Case #{i + 1}: {x} + {y} = {x+y}')
    i += 1

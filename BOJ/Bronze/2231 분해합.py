n = int(input())
result = 0

for i in range(1, n+1) :
    a = list(map(int, str(i)))

    if n == i + sum(a) :
        result = i
        break

print(result)

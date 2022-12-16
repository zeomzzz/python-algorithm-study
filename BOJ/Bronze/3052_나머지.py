lst = []
i = 0

while i < 10 :
    x = int(input())
    a = x % 42

    if a not in lst :
        lst.append(a)

    i += 1

print(len(lst))

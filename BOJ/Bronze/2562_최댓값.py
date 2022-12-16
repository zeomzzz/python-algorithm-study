lst = []
i = 0

while i < 9 :
    x = int(input())
    lst.append(x)
    i += 1

print(max(lst))
print(lst.index(max(lst)) + 1)

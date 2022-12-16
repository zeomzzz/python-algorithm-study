lst = []

for i in range(1, 31) :
    lst.append(i)

for j in range(0, 28) :
    x = int(input())
    lst.remove(x)

print(min(lst))
print(max(lst))

s1 = input()
s2 = input()

lst1 = list(s1)
lst2 = list(s2)

for i in range(len(lst1) - 1, -1, -1) :
    if lst1[i] in lst2 :
        lst2.remove(lst1[i])
        lst1.remove(lst1[i])

print(len(lst1) + len(lst2))

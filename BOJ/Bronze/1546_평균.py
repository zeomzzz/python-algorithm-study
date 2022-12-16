n = int(input())
lst = list(map(int, input().split()))

m = max(lst)

newlst = []

for i in lst :
    newlst.append(i * 100 / m)

print(sum(newlst)/n)

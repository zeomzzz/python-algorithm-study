x = input().upper()
a = list(set(x))
cnt = []

for i in a :
    cnt.append(x.count(i))

if cnt.count(max(cnt)) > 1 :
    print("?")
else :
    print(a[cnt.index(max(cnt))])

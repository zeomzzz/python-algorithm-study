N = int(input())

for t in range(N):
    s1, s2 = map(str, input().split())
    lst1 = sorted(s1)
    lst2 = sorted(s2)

    if lst1 == lst2 :
        print("Possible")
    else :
        print("Impossible")

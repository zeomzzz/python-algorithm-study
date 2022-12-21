n, m = map(int, input().split())
cards = list(map(int, input().split()))
lst = []

for i in range(n-2) :
    for j in range(i+1, n-1) :
        for k in range(j+1, n) :
            sum = cards[i] + cards[j] + cards[k]

            if sum > m :
                continue
            else :
                lst.append(sum)

print(max(lst))

# 풀이 1 : for문 이용

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


# 풀이 2 : itertools 이용

import itertools

n, m = map(int, input().split())
cards = list(map(int, input().split()))
lst = []

for i in itertools.combinations(cards, 3) :
    if sum(i) > m :
        continue
    else :
        lst.append(sum(i))

print(max(lst))

import sys

N = int(sys.stdin.readline().rstrip()) # 카드 수

cards = []

for i in range(1, N + 1) :
    cards.append(i)

print(cards.pop(0), end = " ")

if len(cards) > 0 :
    while len(cards) > 1 :
        cards.append(cards.pop(0))
        print(cards.pop(0), end = " ")

    print(cards[0])

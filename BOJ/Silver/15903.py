import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split()) # n개 카드, m번 합체
cards = list(map(int, input().rstrip().split()))

for _ in range(m) :
    cards.sort()
    cards[0] += cards[1]
    cards[1] = cards[0]

print(sum(cards))

import sys
input = sys.stdin.readline

N = int(input().rstrip()) # 플레이어의 수 N
cards = list(map(int, input().rstrip().split()))
maxx = max(cards)

visited = [0] * (maxx + 1)
for c in cards : visited[c] = 1

scores = [0] * (maxx + 1)

for c in cards :
    tmp = 2

    while c * tmp < maxx + 1 :

        if visited[c * tmp] == 1 :
            scores[c] += 1
            scores[c * tmp] -= 1

        tmp += 1

for c in cards :
    print(scores[c], end = " ")

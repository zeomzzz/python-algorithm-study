import sys

n, k = map(int, sys.stdin.readline().rstrip().split()) # n개 동전으로 k 만듦

coins = []
for _ in range(n) :
    coin = int(sys.stdin.readline().rstrip())
    coins.append(coin)

coins.reverse()

sum = 0 # 동전 개수의 합

for x in coins :
    cnt = k // x
    sum += cnt
    k -= x * cnt

    if k == 0 :
        break

print(sum)

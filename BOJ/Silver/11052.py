n = int(input())
prices = list(map(int, input().split()))
prices.insert(0, 0)

# k 번째는 prices[k], k-1 최대값 + 1 최대값, k-2 최대값 + 2 최대값 ... 중 최대값임
# prices에 최대값을 업데이트 하여도 이후 계산에 영향 미치지 않음

if n > 1 :
  for i in range(2, n + 1) :
    tmp = []
    for k in range(int(i/2) + 1) :
      tmp.append(prices[k] + prices[i - k])
    prices[i] = max(tmp)
  
print(prices[-1])

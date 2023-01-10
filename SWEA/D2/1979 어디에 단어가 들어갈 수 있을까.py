T = int(input())

for t in range(T) :
  N, K = map(int, input().split())
  caseLst = []
  for i in range(N) :
    caseLst.append(list(map(int, input().split())) + [0])

  answer = 0

  # 가로줄 검사
  sumLst = []
  sum = 0
  for j in range(N) :
    for k in range(N + 1) :
      if caseLst[j][k] == 1 :
        sum += 1
      else :
        sumLst.append(sum)
        sum = 0
  answer = sumLst.count(K)

  # 세로줄 검사
  sumLst = []

  caseLst.append([0] * (k + 1))
  for l in range(N + 1) :
    for m in range(N + 1) :
      if caseLst[m][l] == 1 :
        sum += 1
      else :
        sumLst.append(sum)
        sum = 0
  answer += sumLst.count(K)

  print(f'#{t + 1} {answer}')

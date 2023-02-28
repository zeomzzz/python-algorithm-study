n = int(input())
lst = list(map(int, input().split()))

cnt = 0

for i in lst :
  isTrue = True
  if i == 1 :
    isTrue = False
  elif i == 2 :
    pass
  else :
    for j in range(2, i) :
      if i % j == 0 :
        isTrue = False

  if isTrue : cnt += 1

print(cnt)

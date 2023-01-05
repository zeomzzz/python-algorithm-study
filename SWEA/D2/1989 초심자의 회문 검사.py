T = int(input())

for i in range(T) :
  a = input()
  b = a[::-1]

  result = 0
  if a == b :
    result = 1

  print(f'#{i + 1} {result}')

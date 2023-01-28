n = int(input())

first_l = (n - 1) * " " + "*"
print(first_l)

if n != 1 :
  for i in range(2, n) :
    print((n - i) * " " + "*" + (2 * i - 3) * " " + "*")
  last_l = (2 * n - 1) * "*"
  print(last_l)

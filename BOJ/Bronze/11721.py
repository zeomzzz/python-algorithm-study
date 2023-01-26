S = input()

t = len(S) // 10

for i in range(t) :
  print(S[10 * i : 10 * (i + 1)])
print(S[10 * t :])

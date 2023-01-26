N = int(input())
T = 2 * N - 1

for i in range(T) :
  print("*" * (N - abs(- N + 1 + i)), end = "")# 별
  print(" " * abs(2 * (i - N + 1)), end = "") # 공백
  print("*" * (N - abs(- N + 1 + i))) # 별

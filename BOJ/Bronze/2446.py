N = int(input())
T = 2 * N - 1

for i in range(T) :
  print(" " * (N - 1 - abs(N - i - 1)) 
  + "*" * (abs(2 * (N - i - 1)) + 1))

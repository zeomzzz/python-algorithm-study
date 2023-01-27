n = int(input())
line = " " * (n - 1) + "*"

for i in range(n) :
  print(line)
  line = line[1:] + " *"

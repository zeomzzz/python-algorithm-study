import math

N_lst = list(input())
num_lst = [0] * 10

for i in N_lst :
  num_lst[int(i)] += 1

num_lst[6] = math.ceil((num_lst[6] + num_lst[9]) / 2)
num_lst[9] = num_lst[6]

print(max(num_lst))

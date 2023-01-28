S = input()
lst = [0] * 26

for i in S :
  lst[ord(i) - 97] += 1

for s in lst :
    print(s, end = " ")

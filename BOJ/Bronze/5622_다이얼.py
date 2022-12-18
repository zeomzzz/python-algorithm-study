word = input()
num = []

for i in word :
    if i in ['A', 'B', 'C'] : num.append(3)
    elif i in ['D', 'E', 'F'] : num.append(4)
    elif i in ['G', 'H', 'I'] : num.append(5)
    elif i in ['J', 'K', 'L'] : num.append(6)
    elif i in ['M', 'N', 'O'] : num.append(7)
    elif i in ['P', 'Q', 'R', 'S'] : num.append(8)
    elif i in ['T', 'U', 'V'] : num.append(9)
    elif i in ['W', 'X', 'Y', 'Z'] : num.append(10)

print(sum(num))

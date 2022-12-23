x_lst = []
y_lst = []


for i in range(3) :
    a, b = map(int, input().split())

    x_lst.append(a)
    y_lst.append(b)


for x in x_lst :
    if x_lst.count(x) == 1 :
        print(x, end = ' ')

for y in y_lst :
    if y_lst.count(y) == 1 :
        print(y)

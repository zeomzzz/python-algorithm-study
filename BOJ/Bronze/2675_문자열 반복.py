n = int(input())

for i in range(n) :
    x = input()
    answer = ''

    for j in x[2:] :
        answer += j * int(x[0])
    print(answer)

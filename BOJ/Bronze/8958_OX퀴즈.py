n = int(input())

for i in range(n) :
    x = input()
    score = 0
    sumscore = 0

    for j in x :
        if j == 'O' :
            score += 1
        else :
            score = 0
        sumscore += score
        
    print(sumscore)

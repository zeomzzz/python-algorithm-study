t = int(input())

for i in range(t) :
    
    n = int(input())
    result = 0

    for j in range(1, n+1) :
        if j % 2 == 0 :
            j *= -1
        
        result += j
    
    print(f'#{i+1} {result}')

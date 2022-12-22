t = int(input())

for i in range(t) :
    a, b, c, d, e = 0, 0, 0, 0, 0

    n = int(input())
    
    while True :
        if n % 2 == 0 :
            a += 1
            n /= 2
        if n % 3 == 0 :
            b += 1
            n /= 3
        if n % 5 == 0 :
            c += 1
            n /= 5
        if n % 7 == 0 :
            d += 1
            n /= 7
        if n % 11 == 0 :
            e += 1
            n /= 11
        if (n % 2) * (n % 3) * (n % 5) * (n % 7) * (n % 11) == True :
            break
    
    print(f'#{i + 1} {a} {b} {c} {d} {e}')

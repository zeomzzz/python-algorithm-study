X = int(input())
n = 1

while True :
    if X >= n * (n - 1) / 2 + 1 and X <= n * (n + 1) / 2 :
        a = round(X - n * (n - 1) / 2)
        b = round((n + 1) - a)

        if n % 2 == 0 :
            print(str(a) + "/" + str(b))

        else :
            print(str(b) + "/" + str(a))
        
        break
    
    else :
        n += 1

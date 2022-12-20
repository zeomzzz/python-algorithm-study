def f(n) :
    if n == 0 :
        result = 0
    elif n == 1 :
        result = 1
    elif n > 0 :
        result = f(n-1) + f(n-2)
        
    return result

  
x = int(input())

print(f(x))

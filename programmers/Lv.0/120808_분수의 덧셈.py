def solution(denum1, num1, denum2, num2):
    
    a = num1 * num2
    b = denum1 * num2 + denum2 * num1
    c = min(a, b)
    
    for i in range(0, c - 1) :
        if a % (c - i) == 0 and b % (c - i) == 0 :
            a = a // (c - i)
            b = b // (c - i)
    
    answer = [b, a]
    
    return answer

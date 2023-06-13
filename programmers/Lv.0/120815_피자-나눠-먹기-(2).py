def solution(n):
    
    if n % 6 == 0 :
        answer = n / 6
    elif n % 2 == 0 :
        answer = n / 2
    elif n % 3 == 0 :
        answer = n / 3
    else :
        answer = n
    
    return answer

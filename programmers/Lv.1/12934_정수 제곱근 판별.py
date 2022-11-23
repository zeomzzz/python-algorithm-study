def solution(n):
    
    x = int(n ** (1/2))
    
    if n ** (1/2) == x :
        answer = (x + 1) ** 2
    else :
        answer = -1
    
    return answer

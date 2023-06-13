def solution(n):
    
    for i in range(1, 12) :
        i_factorial = 1
        for k in range(1, i+1) :
            i_factorial *= k

        if i_factorial > n :
            answer = i - 1
            break
    
    return answer

def solution(a, b):
    answer = 0
    n = min(a, b)
    
    if a == b :
        answer = a
    else :
        while n <= max(a, b) :
            answer += n
            n += 1
    
    return answer

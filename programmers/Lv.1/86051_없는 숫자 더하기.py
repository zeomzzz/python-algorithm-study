def solution(numbers):
    answer = 0
    
    for i in range(0, 10) :
        answer += i
    
    for j in numbers :
        answer -= j
    
    return answer
